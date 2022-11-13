from typing import Optional, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

notes = []


class Note(BaseModel):
    content: str
    author: Optional[str]
    is_open: bool


@app.get("/", response_model=List[Note])
async def get_notes():
    return notes


@app.post("/")
async def create_note(note: Note):
    notes.append(note)
    return "Success"


@app.get("/{id}")
async def get_note(id: int = Path(..., description="The ID of the note yoy want ti retrieve", gt=0)):
    return notes[id]
