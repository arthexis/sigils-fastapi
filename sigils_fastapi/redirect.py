import sigils
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from urllib.parse import unquote

app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{path:path}")
async def redirect(path: str):
    path = unquote(path)
    print(path)
    path = sigils.splice()
    print(path)
    return RedirectResponse(path)
    

__all__ = ["app"]
