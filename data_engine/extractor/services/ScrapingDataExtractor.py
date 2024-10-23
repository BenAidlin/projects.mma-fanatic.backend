from time import sleep

from ..adapters.AbstractDataExtractor import AbstractDataExtractor
import requests
import jmespath

class ScrapingDataExtractor(AbstractDataExtractor):
    def __init__(self, **kwargs):
        self.url = "https://site.web.api.espn.com/apis/personalized/v2/scoreboard/header?sport=mma&region=us&lang=en&configuration=SITE_DEFAULT&platform=web&buyWindow=1m&showAirings=buy%2Clive%2Creplay&showZipLookup=true&tz=America%2FNew_York&postalCode=38362%2044"


    def extract_data(self):
        leagues = self.__get_year_leagues()
        for league in leagues:
            events = ScrapingDataExtractor.__get_events(league)



    def __get_year_leagues(self):
        try:
            response = requests.get(self.url).json()
            jmespath_query = "[sports[?name == 'mma' || name == 'MMA']][0][0].leagues"
            leagues = jmespath.search(jmespath_query, response)
            return leagues
        except Exception as e:
            return []

    @staticmethod
    def __get_events(league):
        events = []
        for event in league["events"]:
            event.update({"league_id": league["id"]})
            events.append(event)
            ScrapingDataExtractor.__scrape_event(event)
        return events

    @staticmethod
    def __scrape_event(event):
        event_url = a