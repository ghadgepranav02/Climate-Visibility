import os, sys
from flask import request
from src.logger import logging
from src.utils.main_utils import MainUtils
from src.constant import *
from src.exception import VisibilityException
from dataclasses import dataclass


@dataclass
class PredictionPipelineConfig:
    model_path = os.path.join("artifacts","model_trainer","trained_model","model.pkl")


class PredictionPipeline:
    def __init__(self, request: request):
        self.request = request
        self.utils = MainUtils()
        self.prediction_pipeline_config = PredictionPipelineConfig()

    def get_model_path(self):
        try:
            model_path = self.prediction_pipeline_config.model_path
            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"Model file not found: {model_path}. Run /train first to create the model file."
                )
            return model_path
        except Exception as e:
            raise VisibilityException(e, sys)

    def run_pipeline(self):
        try:
            data = dict(self.request.form.items())
            values = data.values()
            model_path = self.get_model_path()
            model = self.utils.load_object(file_path=model_path)
            prediction = model.predict([list(values)])
            return prediction
        except Exception as e:
            raise VisibilityException(e, sys)
            
        

 
        

        