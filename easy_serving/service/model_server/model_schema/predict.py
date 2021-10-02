from pydantic import BaseModel
from typing import List, Union

class GenericResponsePayload(BaseModel):
    data: Union[List[int], List[List[int]]]