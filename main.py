from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse, JSONResponse, HTMLResponse, Response
from fastapi.staticfiles import StaticFiles

from json import load

from uvicorn import run
from loomin.packages import jinki
from loomin.custom.JinkiPostProcessors import PostProcessors

with open("config.json", "r") as file:
    config = load(file)

app = FastAPI(
    docs_url=None,
    redoc_url=None
)

## HOME
## The homepage of the loomin wiki server. This homepage can be modified.

@app.get("/")
async def home():
    return "Loomin Home HTML here"

## WIKI
## i dont need to explain this

@app.get("/wiki")
async def wiki():
    return "selection of wikis here (wikis.json)"

@app.get("/wiki/{wiki}/{content:path}")
async def wiki_content():
    return "wiki shenanigans here"

## ASSETS
## Access assets from the github repository (no long paths)

@app.get("/assets/{wiki}/{filename}")
async def asset():
    return "return asset now (use github api)"

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8080, reload=True, reload_delay=5)