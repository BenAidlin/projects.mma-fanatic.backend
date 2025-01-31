from decouple import config
from fastapi import APIRouter

from bff_service.src.app.infrastructure.redirect_utility import RedirectUtility

router = APIRouter()
schedule_service_url = config("SERVICE_URL_SCHEDULING")


@router.get("/")
def get_schedule():
    return RedirectUtility.redirect_get(f"{schedule_service_url}/schedule")
