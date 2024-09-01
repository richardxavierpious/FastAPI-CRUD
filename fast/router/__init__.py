from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from loginmethods import get_data

templates = Jinja2Templates(directory="templates")

def create_app():
    app = FastAPI()
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(get_data)

    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return "Hello World!"

    @app.get("/home", response_class=HTMLResponse)
    async def homepage(request: Request):
        return templates.TemplateResponse('item.html', {"request": request})

    return app
