from datetime import datetime
from bs4 import BeautifulSoup
import json
import re
from ..adapters.AbstractDataExtractor import AbstractDataExtractor
import requests
import jmespath

from common.adapters.abstract_msg_client import AbstractMsgClient
from ..dependency_injection_service import DIService
from ..models.django_models.extraction_job_model import ExtractionJobModel
from ..models.ScrapingUrl import ScrapingUrl

class ScrapingDataExtractor(AbstractDataExtractor):
    def __init__(self):
        self.url: ScrapingUrl = DIService.resolve("ScrapingUrl")
        self.abstract_msg_client: AbstractMsgClient = DIService.resolve("AbstractMsgClient")


    def extract_data(self):
        events = self.scrape_events()
        self.abstract_msg_client.produce_message(str(events))
        extraction_job_model = ExtractionJobModel(time=datetime.now(), success=True, length=len(str(events)))
        extraction_job_model.save()


    def scrape_events(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            response = requests.get(self.url.url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            script_tags = [tag for tag in soup.findAll('script') if '__espnfitt__' in tag.text]
            if script_tags:
                script_tag = script_tags[0]
            else: return []
            match = re.search(r'window\[\'__espnfitt__\'\]\s*=\s*({.*?})\s*;', script_tag.string, re.DOTALL)
            script_line = match.group(0)
            script_line = script_line.replace('window[\'__espnfitt__\']=', '')
            script_line = script_line[0:-1]
            json_data = json.loads(script_line)
            jmespath_query = "page.content.events.values(@)[].{id: id, link: link, date: date, name: name, is_completed: completed}"
            events = jmespath.search(jmespath_query, json_data)
            return events
        except Exception as e:
            return []
