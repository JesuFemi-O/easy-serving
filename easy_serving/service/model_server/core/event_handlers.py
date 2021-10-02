from typing import Callable
import os

from fastapi import FastAPI
from loguru import logger
from easy_serving.service.model_server.ml_service.models import GenericModelService

def _startup_model(app: FastAPI) -> None:
    model_path = os.environ.get('MODEL_BASE_PATH')
    model_instance = GenericModelService(model_path)
    app.state.model = model_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        # invoke the start model handler
        _startup_model(app)
    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app sutdown handler.")
        # invoke the shutdown model handler
        _shutdown_model(app)
    return shutdown