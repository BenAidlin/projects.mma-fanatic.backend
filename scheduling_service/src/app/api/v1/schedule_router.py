from fastapi import APIRouter
from fastapi_restful.cbv import cbv

from scheduling_service.src.app.domains.schedule.facades.schedule_facade import ScheduleFacade
from scheduling_service.src.app.infrastructure.dependency_injection_container import DIContainer

router = APIRouter()

@cbv(router)
class ScheduleAPI:
    def __init__(self):
        self.schedule_facade: ScheduleFacade = DIContainer.resolve('ScheduleFacade')

    @router.get('/')
    def get_schedule(self):
        return [e for e in self.schedule_facade.get_schedule()]

    @router.post('/')
    def create_schedule(self):
        self.schedule_facade.generate_schedule()
