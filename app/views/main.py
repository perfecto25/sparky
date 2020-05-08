from app import app, templates
from fastapi import Request

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

