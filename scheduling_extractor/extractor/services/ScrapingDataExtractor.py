import threading
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from typing import List

from bs4 import BeautifulSoup
import json
import re
from ..adapters.AbstractDataExtractor import AbstractDataExtractor
import requests
import jmespath

from common.adapters.abstract_msg_client import AbstractMsgClient
from ..dependency_injection_service import DIService
from ..models.django_models.event_model import ExtractedEventModel
from ..models.django_models.extraction_job_model import ExtractionJobModel


class ScrapingDataExtractor(AbstractDataExtractor):
    @staticmethod
    def _get_espn_base_url() -> str:
        return "https://www.espn.com"

    def __init__(self):
        self.scraping_urls: List[str] = [f'/mma/schedule/_/year/{datetime.now().year}', f'/mma/schedule/_/year/{datetime.now().year+1}']
        self.abstract_msg_client: AbstractMsgClient = DIService.resolve("AbstractMsgClient")
        self.lock = threading.RLock()

    def extract_data(self):
        events = self._scrape_events()
        self.abstract_msg_client.produce_message(str([event.to_mongo() for event in events]))
        extraction_job_model = ExtractionJobModel(time=datetime.now(), success=True, length=len(str(events)))
        extraction_job_model.save()


    def _scrape_events(self) -> List[ExtractedEventModel]:
        try:
            headers = self._get_headers_for_scraping()
            events: List[ExtractedEventModel] = []
            for scraping_url in self.scraping_urls:
                url = self._get_espn_base_url() + scraping_url
                response = requests.get(url, headers=headers)
                json_data = self._extract_espn_scraping_logic(response=response)
                jmespath_query = "page.content.events.values(@)[].{id: espn_id, link: link, event_date: date, name: name, is_completed: completed}"
                events_dictionaries = jmespath.search(jmespath_query, json_data)
                events.extend([ExtractedEventModel(**event) for event in events_dictionaries])

            events = list(filter(lambda event: not event.is_completed, events))
            futures = []
            with ThreadPoolExecutor() as executor:
                for event in events:
                    futures.append(executor.submit(self._scrape_event, event))
            for future in futures: future.result()
            return events
        except Exception as e:
            return []


    def _scrape_event(self, event: ExtractedEventModel):
        if not event.link:
            event.cards = None
        else:
            event.cards = self._scrape_cards(event.link)


    def _scrape_cards(self, link: str) -> dict:
        headers = self._get_headers_for_scraping()
        response = requests.get(self._get_espn_base_url() + link, headers=headers)
        json_data = self._extract_espn_scraping_logic(response=response)
        jmespath_query = "page.content.gamepackage.cardSegs"
        cards = jmespath.search(jmespath_query, json_data)
        return cards


    @staticmethod
    def _get_headers_for_scraping() -> dict:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        return headers

    @staticmethod
    def _extract_espn_scraping_logic(response: requests.Response) -> List[dict]:
        soup = BeautifulSoup(response.text, 'lxml')
        script_tags = [tag for tag in soup.findAll('script') if '__espnfitt__' in tag.text]
        if script_tags:
            script_tag = script_tags[0]
        else:
            return []
        match = re.search(r'window\[\'__espnfitt__\'\]\s*=\s*({.*?})\s*;', script_tag.string, re.DOTALL)
        script_line = match.group(0)
        script_line = script_line.replace('window[\'__espnfitt__\']=', '')
        script_line = script_line[0:-1]
        json_data = json.loads(script_line)
        return json_data
