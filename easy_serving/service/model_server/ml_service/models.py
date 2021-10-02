import joblib
import numpy as np
from typing import List
from loguru import logger
from easy_serving.service.model_server.api.routes import prediction
from easy_serving.service.model_server.model_schema.payload import GenericPayload
from easy_serving.service.model_server.core.messages import NO_VALID_PAYLOAD

class GenericModelService(object):
    def __init__(self, path):
        self.path = path
        self._load_model()
    
    def _load_model(self):
        self.model = joblib.load(self.path)
    
    def _pre_process(self, payload: GenericPayload) -> List:
        logger.debug("Pre-processing payload.")
        logger.info("data", payload.data)
        if isinstance(payload.data[0], list):
            result = np.asarray(payload.data)
        else:
            result = np.asarray(payload.data).reshape(1, -1)
        return result
    
    def _predict(self, features: np.ndarray) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result
    
    def predict(self, payload: GenericPayload):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(f"Prediction: {prediction}")
        return {"data":list(prediction)}