from decouple import config
from typing import Any
from fastapi import APIRouter, Body

from bff_service.src.app.infrastructure.redirect_utility import RedirectUtility

router = APIRouter()
predictions_service_url = config("SERVICE_URL_PREDICTIONS")
predictions_endpoints_route = f"{predictions_service_url}/predictions"


@router.post("/")
def create_prediction(prediction: Any = Body(...)):
    return RedirectUtility.redirect_post(f"{predictions_endpoints_route}/", prediction)


@router.get("/{user_id}")
def get_predictions(user_id: str):
    return RedirectUtility.redirect_get(f"{predictions_endpoints_route}/{user_id}")


@router.put("/")
def update_prediction(prediction: Any = Body(...)):
    return RedirectUtility.redirect_put(f"{predictions_endpoints_route}/", prediction)


@router.delete("/")
def remove_predictions(predictions: Any = Body(...)):
    return RedirectUtility.redirect_delete(
        f"{predictions_endpoints_route}/", predictions
    )
