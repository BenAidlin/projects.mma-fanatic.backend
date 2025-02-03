from pydantic import BaseModel


class User(BaseModel):
    id: str | None
    email: str | None
    name: str | None
    given_name: str | None
    family_name: str | None
    picture: str | None

    @classmethod
    def from_dict(cls, dict_: dict):
        return User(
            id=dict_.get("id"),
            email=dict_.get("email"),
            name=dict_.get("name"),
            given_name=dict_.get("given_name"),
            family_name=dict_.get("family_name"),
            picture=dict_.get("picture"),
        )
