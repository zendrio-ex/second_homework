import os
from catboost import CatBoostRegressor
from src.config import settings

# It can be done via import gdown
command = f"gdown --folder '{settings['google_drive']}'"
os.system(command)

model = CatBoostRegressor()
model.load_model('./model/model.cbm')
