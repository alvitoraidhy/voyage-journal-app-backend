from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi import APIRouter, Depends
from typing import List

from models import User, Note
from ..auth.dependencies import active_user
from .requests import NoteIn, NoteUpdateIn
from .responses import NoteOut

router = APIRouter()


# Routes


@router.get("/", response_model=List[NoteOut])
async def read_notes(user: User = Depends(active_user)):
    await user.fetch_related("notes")

    response = [
        {"id": note.id, "title": note.title, "body": note.body} for note in user.notes
    ]

    return JSONResponse(response, 200)


@router.post("/", response_model=NoteOut)
async def create_note(form: NoteIn, user: User = Depends(active_user)):
    note = Note(title=form.title, body=form.body, user_id=user.id)

    await note.save()

    response = {"id": note.id, "title": note.title, "body": note.body}

    return JSONResponse(response, 201)


@router.get("/{note_id}", response_model=NoteOut)
async def read_note(note_id: int, user: User = Depends(active_user)):
    note = await Note.get_or_none(id=note_id, user_id=user.id)

    if note is None:
        raise HTTPException(404, "note not found or inaccessible")

    response = {"id": note.id, "title": note.title, "body": note.body}

    return JSONResponse(response, 200)


@router.put("/{note_id}", response_model=NoteOut)
async def update_note(
    note_id: int, form: NoteUpdateIn, user: User = Depends(active_user)
):
    note = await Note.get_or_none(id=note_id, user_id=user.id)

    if note is None:
        raise HTTPException(404, "note not found or inaccessible")

    note.title = form.title or note.title
    note.body = form.body or note.body

    await note.save()

    response = {"id": note.id, "title": note.title, "body": note.body}

    return JSONResponse(response, 200)


@router.delete("/{note_id}")
async def delete_note(note_id: int, user: User = Depends(active_user)):
    note = await Note.get_or_none(id=note_id, user_id=user.id)

    if note is None:
        raise HTTPException(404, "note not found or inaccessible")

    await note.delete()

    return Response(status_code=204)
