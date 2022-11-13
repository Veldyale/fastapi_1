from fastapi import FastAPI
from endpoints import notes

app = FastAPI()

app.include_router(notes.router)
