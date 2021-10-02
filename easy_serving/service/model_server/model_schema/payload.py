from pydantic import BaseModel
from typing import List, Union

class GenericPayload(BaseModel):
     data: Union[List[int], List[List[int]]]