from easy_serving.service.model_server.model_schema.heartbeat import HeatbeatResult
from fastapi import APIRouter


router = APIRouter()


@router.get('/heartbeat', response_model=HeatbeatResult, name="heartbeat")
def get_heartbeat() -> HeatbeatResult:
    heartbeat = HeatbeatResult(is_alive=True)
    return heartbeat
