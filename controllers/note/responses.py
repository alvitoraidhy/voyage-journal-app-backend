from pydantic import BaseModel


class NoteOut(BaseModel):
    id: int
    title: str
    body: str
