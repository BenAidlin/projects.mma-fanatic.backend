from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from ..adapters.AbstractDataExtractor import AbstractDataExtractor
from ..services.ScrapingDataExtractor import ScrapingDataExtractor

class ExtractorView(APIView):

    def __init__(self, data_extractor: AbstractDataExtractor = None):
        if not data_extractor:
            data_extractor = ScrapingDataExtractor()
        self.data_extractor = data_extractor

    def get(self, request: Request) -> Response:
        scraping_data = self.data_extractor.extract_data()
        return Response({'message': 'Hello, World!'})