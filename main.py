# GOOOOOOOOOOOOOAAAAAAAAAAALLLLLLLLLL!!! (s)
# - new and cleaner api (and also document it properly ig)
# - be able to STILL run on serverless functions (make it exclusively made for deta???)
# - be able to manage edits by people online publicly (id assigned by IP? or randomly generated... maybe even masked ip...)
# - better frontend (since i suck and lost the excalidraw board.......) (could also be modern ui or something)

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse, JSONResponse, HTMLResponse, Response
from fastapi.staticfiles import StaticFiles

from uvicorn import run

app = FastAPI(
    docs_url=None,
    redoc_url=None
)

@app.get("/")
async def homepage():
    return "Homepage Here lol"

if __name__ == "__main__":
    #                                           disable these when the backend is done
    run("main:app", host="0.0.0.0", port=69420, reload=True, reload_delay=5)