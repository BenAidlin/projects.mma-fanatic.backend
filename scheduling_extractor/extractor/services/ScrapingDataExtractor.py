from datetime import datetime

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
        leagues = self.__get_year_leagues()
        extraction_job_model = ExtractionJobModel(time=datetime.now(), success=True, length=len(str(leagues)))
        extraction_job_model.save()


    def __get_year_leagues(self):
        try:
            response = requests.get(self.url.url).json()
            jmespath_query = "[sports[?name == 'mma' || name == 'MMA']][0][0].leagues"
            leagues = jmespath.search(jmespath_query, response)
            return leagues
        except Exception as e:
            return []
