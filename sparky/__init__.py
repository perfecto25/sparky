from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./sparky/static"), name="static")
templates = Jinja2Templates(directory="./sparky/templates")

from sparky.views import main, errors, tasks