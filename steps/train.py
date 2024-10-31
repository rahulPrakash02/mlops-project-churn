import yaml
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os

class Trainer:
    def __init__(self):
        self.config = self.load_config()
        self.model_name = self.config['model']['name']
        self.model_params = self.config['model']['params']
        self.model_path = self.config['model']['store_path']
        self.pipeline = self.create_pipeline()

    def load_config(self):
        with open('config.yaml', 'r') as config_file:
            return yaml.safe_load(config_file)
        
    def create_pipeline(self):
        
        model_map = {
            'LogisticRegression': LogisticRegression,
        }
    
        model_class = model_map[self.model_name]
        model = model_class(**self.model_params)

        pipeline = Pipeline([
            ('model', model)
        ])

        return pipeline

    def feature_target_separator(self, data):
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        return X, y

    def train_model(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    def save_model(self):
        model_file_path = os.path.join(self.model_path, 'model.pkl')
        os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
        joblib.dump(self.pipeline, model_file_path)