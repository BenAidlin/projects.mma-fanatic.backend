from typing import Any

import fastapi
import requests


class RedirectUtility:
    SOMETHING_WENT_WRONG = {"Message": "Something went wrong"}
    EMPTY_RESPONSE = {"Message": "Empty response"}

    @classmethod
    def handle_response(
        cls, response: requests.Response
    ) -> fastapi.responses.JSONResponse:
        if response.status_code == 200:
            try:
                return fastapi.responses.JSONResponse(
                    content=response.json(),
                    status_code=response.status_code,
                )
            except Exception as e:
                return fastapi.responses.JSONResponse(
                    content=cls.EMPTY_RESPONSE, status_code=response.status_code
                )
        else:
            return fastapi.responses.JSONResponse(
                content=cls.SOMETHING_WENT_WRONG, status_code=response.status_code
            )

    @classmethod
    def redirect_get(cls, endpoint: str):
        return cls.handle_response(requests.get(endpoint, verify=False))

    @classmethod
    def redirect_post(cls, endpoint: str, payload: Any):
        return cls.handle_response(requests.post(endpoint, verify=False, json=payload))

    @classmethod
    def redirect_put(cls, endpoint: str, payload: Any):
        return cls.handle_response(requests.put(endpoint, verify=False, json=payload))

    @classmethod
    def redirect_delete(cls, endpoint: str, payload: Any):
        return cls.handle_response(
            requests.delete(endpoint, verify=False, json=payload)
        )
