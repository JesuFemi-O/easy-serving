from pydantic import BaseModel


class HeatbeatResult(BaseModel):
    is_alive: bool