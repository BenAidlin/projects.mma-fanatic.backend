from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

class ExtractorView(APIView):
    def get(self, request: Request) -> Response:
        print('get endpoint')
        return Response({'message': 'Hello, World!'})