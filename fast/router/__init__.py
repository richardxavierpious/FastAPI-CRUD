from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


from router.login_methods import get_data

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

    @app.get("/")
    def home():
        return "Hello World!"

    @app.get("/home")
    def homepage():
        return templates.TemplateResponse('item.html')

    return app