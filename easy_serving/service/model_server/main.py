from fastapi import FastAPI
from easy_serving.service.model_server.core.config import (
    API_PREFIX, APP_NAME, APP_VERSION, IS_DEBUG)
from easy_serving.service.model_server.api.routes.router import api_router

from easy_serving.service.model_server.core.event_handlers import (
    start_app_handler, stop_app_handler)
import uvicorn


def get_app() -> FastAPI:
    # these values will change
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fast_app.include_router(api_router, prefix=API_PREFIX)
    # add the router

    # add event handlers - invoke handlers when startup and shutdown events occur
    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    return fast_app

app = get_app()

def run_dev_server():
    app = get_app()
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")