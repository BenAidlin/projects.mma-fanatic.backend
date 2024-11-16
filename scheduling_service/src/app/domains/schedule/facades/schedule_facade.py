from scheduling_service.src.app.domains.schedule.services.scheduling_extraction_service import \
    AbstractSchedulingExtractionService
from scheduling_service.src.app.infrastructure.dependency_injection_container import DIContainer


class ScheduleFacade:
    def __init__(self, scheduling_extraction_service: AbstractSchedulingExtractionService=None):
        self.schedule_service: AbstractSchedulingExtractionService = scheduling_extraction_service
        if not self.schedule_service:
            self.schedule_service: AbstractSchedulingExtractionService = DIContainer.resolve('AbstractSchedulingExtractionService')

    def generate_schedule(self):
        return self.schedule_service.extract_general_schedule()

    def get_schedule(self):
        full_schedule = self.schedule_service.get_schedule()
        return full_schedule