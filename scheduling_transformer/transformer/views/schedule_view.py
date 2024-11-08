from rest_framework.response import Response
from rest_framework.views import APIView

from ..dependency_injection_service import DIService
from ..services.abstract_scheduling_service import AbstractSchedulingService


class ScheduleView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.abstract_schedule_service: AbstractSchedulingService = DIService.resolve('AbstractSchedulingService')

    def get(self, request):
        return Response(self.abstract_schedule_service.get_current_schedule())
