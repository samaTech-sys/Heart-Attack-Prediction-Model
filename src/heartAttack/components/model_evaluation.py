import os 
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
import mlflow
from pathlib import Path
import mlflow.sklearn
from heartAttack.utils.common import save_json
from heartAttack.entity.entity_config import ModelEvaluationConfig

class ModelEvaluation: 
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, pred): 
        rmse = np.sqrt(mean_absolute_error(actual, pred))
        mse = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mse, r2

    def log_into_mlflow(self): 
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column], axis =1)
        test_y = test_data[self.config.target_column]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            (rmse, mse, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            #saving metrics as local 
            scores = {"rmse": rmse, "mse": mse, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mse", mse)
            mlflow.log_metric("r2", r2)
            
            #model registry does not work with filestore
            if tracking_url_type_store != "file":
                #Register the model 
                #There are other ways to use the model registry that depend on the use case
                #Please refer to the doc for more information 
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else: 
                mlflow.sklearn.log_model(model, "model")