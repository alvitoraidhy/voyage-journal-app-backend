from pydantic import BaseModel, constr


class LoginIn(BaseModel):
    username: str
    password: str


class RegisterIn(BaseModel):
    username: constr(min_length=1, max_length=16, regex=r"^[a-z]*$")
    password: constr(min_length=1, max_length=16, regex=r"^\S*$")
