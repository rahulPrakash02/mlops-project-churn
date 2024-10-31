import mlflow
import mlflow.sklearn
from datetime import datetime
import yaml
from steps.ingest import Ingestion
from steps.clean import Cleaner
from steps.train import Trainer
from steps.predict import Predictor

def main():

    #Import Configuration Data
    with open("config.yaml", "r") as file:
         config = yaml.safe_load(file)
         
    # Define names for logging and mlflow
    experiment_name = "churn-prediction-logistic-regression"
    run_name = datetime.now().strftime("%Y%m%d_%H%M%S")

    #Set Experiment Name
    mlflow.set_experiment(experiment_name)
    with mlflow.start_run(run_name = run_name) as mlflow_run:

        # Load data
        ingestion = Ingestion()  
        train, test = ingestion.load_data()
        print("Data ingestion completed successfully")

        # Clean data
        cleaner = Cleaner()
        train_data = cleaner.clean_data(train)
        test_data = cleaner.clean_data(test)
        print("Data cleaning completed successfully")

        # Prepare and train model
        trainer = Trainer()
        X_train, y_train = trainer.feature_target_separator(train_data)
        trainer.train_model(X_train, y_train)
        trainer.save_model()
        print("Model training completed successfully")

        # Evaluate model
        predictor = Predictor()
        X_test, y_test = predictor.feature_target_separator(test_data)
        accuracy, class_report, report, roc_auc_score = predictor.evaluate_model(X_test, y_test)
        print("Model evaluation completed successfully")

        mlflow.set_tag('Author', config['author'])
        mlflow.set_tag('Model', config['model']['name'])
            
        # Log metrics
        model_params = config['model']['params']
        mlflow.log_params(model_params)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("roc", roc_auc_score)
        mlflow.log_metric('precision', report['weighted avg']['precision'])
        mlflow.log_metric('recall', report['weighted avg']['recall'])
        mlflow.sklearn.log_model(trainer.pipeline, "model")
                    
        # Register the model
        model_name = "Churn Model" 
        model_uri = f"runs:/{mlflow_run.info.run_id}/model"
        mlflow.register_model(model_uri, model_name)
        print("MLflow tracking completed successfully")
        
        # Print evaluation results
        print("\n============= Model Evaluation Results ==============")
        print(f"Model: {trainer.model_name}")
        print(f"Accuracy Score: {accuracy:.4f}, ROC AUC Score: {roc_auc_score:.4f}")
        print(f"\n{class_report}")
        print("=====================================================\n")

if __name__ == "__main__":
    main()