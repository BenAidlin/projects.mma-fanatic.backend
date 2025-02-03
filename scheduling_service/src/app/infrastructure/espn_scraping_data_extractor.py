import threading
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from typing import List

from bs4 import BeautifulSoup
import json
import re
import requests
import jmespath

from scheduling_service.src.app.domains.schedule.adapters.abstract_data_extractor import AbstractDataExtractor
from scheduling_service.src.app.domains.schedule.models.event_model import (
    CardModel,
    EventModel,
    FightModel,
    FighterStats,
    FighterModel,
)


class EspnScrapingDataExtractor(AbstractDataExtractor):
    @staticmethod
    def _get_espn_base_url() -> str:
        return "https://www.espn.com"

    def __init__(self):
        self.scraping_url_base = f"/mma/schedule/_/year/"
        self.lock = threading.RLock()

    def extract_data(self, years: list[int] = None) -> list[EventModel]:
        return self._scrape_events(years=years)

    def _scrape_events(self, years: list[int] = None) -> list[EventModel]:
        try:
            headers = self._get_headers_for_scraping()
            events: list[dict] = []
            scraping_urls = [
                f"{self.scraping_url_base}{datetime.now().year}",
                f"{self.scraping_url_base}{datetime.now().year+1}",
            ]
            if years:
                scraping_urls.extend(
                    f"{self.scraping_url_base}{year}/league/ufc" for year in years
                )

            for scraping_url in set(scraping_urls):
                try:
                    url = self._get_espn_base_url() + scraping_url
                    response = requests.get(url, headers=headers, verify=False)

                    json_data = self._extract_espn_scraping_logic(response=response)
                    jmespath_query = "page.content.events.values(@)[].{original_id: id, link: link, event_date: date, name: name, is_completed: completed, postponed_or_canceled: isPostponedOrCanceled}"
                    events_dictionaries = jmespath.search(jmespath_query, json_data)
                    events.extend([event for event in events_dictionaries])
                except:
                    continue
            futures = []
            with ThreadPoolExecutor() as executor:
                for event in events:
                    futures.append(executor.submit(self._scrape_event, event))
            for future in futures: future.result()
            return self._to_model(events)
        except Exception as e:
            return []

    def _scrape_event(self, event: dict):
        if not event['link']:
            event['cards'] = None
        else:
            event['cards'] = self._scrape_cards(event['link'])

    def _scrape_cards(self, link: str) -> dict:
        try:
            headers = self._get_headers_for_scraping()
            response = requests.get(
                self._get_espn_base_url() + link, headers=headers, verify=False
            )
            json_data = self._extract_espn_scraping_logic(response=response)
            jmespath_query = "page.content.gamepackage.cardSegs"
            cards = jmespath.search(jmespath_query, json_data)
            return cards
        except Exception as e:
            return {}

    def _event_to_model(self, event: dict) -> EventModel:
        try:
            return EventModel(
                id=None,
                original_id=event.get("original_id"),
                is_completed=event.get("is_completed"),
                postponed_or_canceled=event.get("postponed_or_canceled"),
                event_date=event.get("event_date"),
                name=event.get("name"),
                cards=(
                    [
                        CardModel(
                            id=None,
                            original_id=c.get("id"),
                            hdr=c.get("hdr"),
                            status=c.get("status"),
                            mtchs=(
                                [
                                    FightModel(
                                        id=None,
                                        original_id=f.get("id"),
                                        awy=(
                                            FighterModel(
                                                id=None,
                                                original_id=(f["awy"].get("id")),
                                                gender=(f["awy"].get("gndr")),
                                                country=(f["awy"].get("country")),
                                                first_name=(f["awy"].get("frstNm")),
                                                last_name=(f["awy"].get("lstNm")),
                                                display_name=(f["awy"].get("dspNm")),
                                                rec=(f["awy"].get("rec")),
                                                short_display_name=(
                                                    f["awy"].get("shrtDspNm")
                                                ),
                                                stats=(
                                                    FighterStats(
                                                        age=f["awy"]["stats"].get(
                                                            "age"
                                                        ),
                                                        ht=(
                                                            f["awy"]["stats"].get("ht")
                                                        ),
                                                        wt=(
                                                            f["awy"]["stats"].get("wt")
                                                        ),
                                                        rch=(
                                                            f["awy"]["stats"].get("rch")
                                                        ),
                                                        sigstrkacc=(
                                                            f["awy"]["stats"].get(
                                                                "sigstrkacc"
                                                            )
                                                        ),
                                                        sigstrklpm=(
                                                            f["awy"]["stats"].get(
                                                                "sigstrklpm"
                                                            )
                                                        ),
                                                        stnce=(
                                                            f["awy"]["stats"].get(
                                                                "stnce"
                                                            )
                                                        ),
                                                        subavg=(
                                                            f["awy"]["stats"].get(
                                                                "subavg"
                                                            )
                                                        ),
                                                        tdacc=(
                                                            f["awy"]["stats"].get(
                                                                "tdacc"
                                                            )
                                                        ),
                                                        tdavg=(
                                                            f["awy"]["stats"].get(
                                                                "tdavg"
                                                            )
                                                        ),
                                                        odds=(
                                                            f["awy"]["stats"].get(
                                                                "odds"
                                                            )
                                                        ),
                                                    )
                                                    if f["awy"].get("stats")
                                                    else None
                                                ),
                                            )
                                            if f["awy"]
                                            else None
                                        ),
                                        hme=(
                                            FighterModel(
                                                id=None,
                                                original_id=(f["hme"].get("id")),
                                                gender=(f["hme"].get("gndr")),
                                                country=(f["hme"].get("country")),
                                                first_name=(f["hme"].get("frstNm")),
                                                last_name=(f["hme"].get("lstNm")),
                                                display_name=(f["hme"].get("dspNm")),
                                                rec=(f["hme"].get("rec")),
                                                short_display_name=(
                                                    f["hme"].get("shrtDspNm")
                                                ),
                                                stats=(
                                                    FighterStats(
                                                        age=f["hme"]["stats"].get(
                                                            "age"
                                                        ),
                                                        ht=(
                                                            f["hme"]["stats"].get("ht")
                                                        ),
                                                        wt=(
                                                            f["hme"]["stats"].get("wt")
                                                        ),
                                                        rch=(
                                                            f["hme"]["stats"].get("rch")
                                                        ),
                                                        sigstrkacc=(
                                                            f["hme"]["stats"].get(
                                                                "sigstrkacc"
                                                            )
                                                        ),
                                                        sigstrklpm=(
                                                            f["hme"]["stats"].get(
                                                                "sigstrklpm"
                                                            )
                                                        ),
                                                        stnce=(
                                                            f["hme"]["stats"].get(
                                                                "stnce"
                                                            )
                                                        ),
                                                        subavg=(
                                                            f["hme"]["stats"].get(
                                                                "subavg"
                                                            )
                                                        ),
                                                        tdacc=(
                                                            f["hme"]["stats"].get(
                                                                "tdacc"
                                                            )
                                                        ),
                                                        tdavg=(
                                                            f["hme"]["stats"].get(
                                                                "tdavg"
                                                            )
                                                        ),
                                                        odds=(
                                                            f["hme"]["stats"].get(
                                                                "odds"
                                                            )
                                                        ),
                                                    )
                                                    if f["hme"].get("stats")
                                                    else None
                                                ),
                                            )
                                            if f["hme"]
                                            else None
                                        ),
                                        nte=f.get("nte"),
                                        # status starting with in + ... R3
                                        status=f.get("status", {"state": None}).get(
                                            "state", ""
                                        )
                                        + "---"
                                        + f.get("status", {"state": None}).get(
                                            "det", ""
                                        ),
                                        dt=f.get("dt"),
                                    )
                                    for f in c["mtchs"]
                                ]
                                if c["mtchs"]
                                else None
                            ),
                        )
                        for c in event["cards"]
                    ]
                    if event["cards"]
                    else None
                ),
            )
        except Exception as e:
            return None

    def _to_model(self, events: list[dict]) -> list[EventModel]:
        convert = [self._event_to_model(event) for event in events]
        return [c for c in convert if c]

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
