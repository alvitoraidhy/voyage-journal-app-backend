from pydantic import BaseModel


class TokenOut(BaseModel):
    token: str


class UserOut(BaseModel):
    username: str
