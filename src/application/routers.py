from fastapi import APIRouter
import os
import toml
import pandas as pd
import numpy as np
from src.application.utils import PredictionResponse, request_id, model, DataPayload, cat_list, num_list
from catboost import FeaturesData, Pool
from loguru import logger

router = APIRouter()
info_router = APIRouter(prefix='/info')


@info_router.get('/version', tags=['Info'])
def version():
    path = os.path.join(os.getcwd(), 'pyproject.toml')
    parsed_pyproject = toml.load(path)
    return {'version': parsed_pyproject['tool']['poetry']['version']}


@router.post("/prediction",
             response_model=PredictionResponse,
             description="""return prediction"""
             )
def get_prediction(request: DataPayload):
    data = pd.DataFrame(request.data, index=[0])
    
    data = Pool(data=FeaturesData(num_feature_data=np.float32(data[num_list].values),
                                  cat_feature_data=data[cat_list].astype(str).values))
    result = model.predict(data)[0]
    result = 0.0 if result < 0.0 else 2.0 if result > 2.0 else result

    return {
        "requestId": request_id.get(),
        "data": {
            "prediction": result
        }
    }


@router.get("/",
            description="""return information"""
            )
def get_docs():
    return {
        "requestId": request_id.get(),
        "information": "prediction"
    }
