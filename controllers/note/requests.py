from pydantic import BaseModel, constr
from typing import Optional


class NoteIn(BaseModel):
    title: constr(min_length=1, max_length=255)
    body: str


class NoteUpdateIn(BaseModel):
    title: Optional[constr(min_length=1, max_length=255)]
    body: Optional[str]
