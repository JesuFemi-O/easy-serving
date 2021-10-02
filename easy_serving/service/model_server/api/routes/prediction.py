from fastapi import APIRouter
from starlette.requests import Request

# from easy_serving.service.model_server.core import security
from easy_serving.service.model_server.model_schema.payload import GenericPayload
from easy_serving.service.model_server.model_schema.predict import GenericResponsePayload
#from zed_server.models.prediction import HousePredictionResult
from easy_serving.service.model_server.ml_service.models import GenericModelService

router = APIRouter()


@router.post("/predict", response_model=GenericResponsePayload, name="predict")
def post_predict(
    request: Request,
    data: GenericPayload = None
) -> GenericResponsePayload:

    model: GenericModelService = request.app.state.model
    prediction: GenericResponsePayload = model.predict(data)

    return prediction
