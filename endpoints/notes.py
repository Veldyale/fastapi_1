from typing import Optional, List
import fastapi
from fastapi import Path
from pydantic import BaseModel

router = fastapi.APIRouter()
notes = []


class Note(BaseModel):
    content: str
    author: Optional[str]
    is_open: bool


@router.get("/", response_model=List[Note])
async def get_notes():
    return notes


@router.post("/")
async def create_note(note: Note):
    notes.append(note)
    return "Success"


@router.get("/{id}")
async def get_note(id: int = Path(..., description="The ID of the note yoy want ti retrieve")):
    return notes[id]
