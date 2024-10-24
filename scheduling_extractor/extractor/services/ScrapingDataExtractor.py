from datetime import datetime
from time import sleep

from ..adapters.AbstractDataExtractor import AbstractDataExtractor
import requests
import jmespath

from ..models.extraction_job_model import ExtractionJobModel
from common.adapters.abstract_msg_client import AbstractMsgClient
from common.implementations.kafka_client import KafkaClient
from decouple import config

class ScrapingDataExtractor(AbstractDataExtractor):
    def __init__(self, abstract_msg_client: AbstractMsgClient):
        self.url = "https://site.web.api.espn.com/apis/personalized/v2/scoreboard/header?sport=mma&region=us&lang=en&configuration=SITE_DEFAULT&platform=web&buyWindow=1m&showAirings=buy%2Clive%2Creplay&showZipLookup=true&tz=America%2FNew_York&postalCode=38362%2044"
        self.abstract_msg_client = abstract_msg_client if abstract_msg_client is not None else\
            KafkaClient(config('KAFKA_BOOTSTRAP_SERVERS'), config('KAFKA_TOPIC'), config('KAFKA_USERNAME'), config('KAFKA_PASSWORD'))


    def extract_data(self):
        leagues = self.__get_year_leagues()
        for league in leagues:
            events = ScrapingDataExtractor.__get_events(league)
        extraction_job_model = ExtractionJobModel(time=datetime.now(), success=True, length=len(str(leagues)))
        extraction_job_model.save()

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
        pass