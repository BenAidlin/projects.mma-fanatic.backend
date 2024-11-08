from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from ..adapters.AbstractDataExtractor import AbstractDataExtractor
from ..dependency_injection_service import DIService

class ExtractorView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_extractor: AbstractDataExtractor = DIService.resolve("AbstractDataExtractor")

    def get(self, request: Request) -> Response:
        scraping_data = self.data_extractor.extract_data()
        return Response({'message': 'Done!'})