import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def run_pipeline(self):
        try:
            # Etapa 1: Ingestão de dados
            logging.info("Iniciando a ingestão de dados")
            train_data, test_data = self.data_ingestion.initiate_data_ingestion()
            logging.info("Ingestão de dados concluída")

            # Etapa 2: Transformação de dados
            logging.info("Iniciando a transformação de dados")
            train_arr, test_arr, preprocessor = self.data_transformation.initiate_data_transformation(train_data, test_data)
            logging.info("Transformação de dados concluída")

            # Salvar o pré-processador
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            save_object(preprocessor_path, preprocessor)
            logging.info(f"Pré-processador salvo em: {preprocessor_path}")

            # Etapa 3: Treinamento do modelo
            logging.info("Iniciando o treinamento do modelo")
            model, best_model_r2_score = self.model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Treinamento concluído. Melhor modelo com R2 Score: {best_model_r2_score}")

            # Salvar o modelo treinado
            model_path = os.path.join("artifacts","model.pkl")
            save_object(model_path, model)
            logging.info(f"Modelo salvo em: {model_path}")

        except Exception as e:
            raise CustomException(e, sys)