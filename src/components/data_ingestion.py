import pandas as pd
import numpy as np

from src.logger import logging
from src.exception import customerException

import os 
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started") 

        try:
            data = pd.read_csv(Path(os.path.join("notebook/data","gemstone.csv")))
            logging.info("i have read data as a df")

            os.makedirs(os.path.dirname(os.path_join(self.ingestion_config.raw_data_path)),
                        exist_ok=True)
            
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("I have saved the raw dataset in artifact folder")

            logging.info("Here I have Performed train_test_split")


            train_data,test_data = train_test_split(data,test_size=0.25)
            logging.info("Train_test_split Completed")
            
            train_data.to_csv(self.ingestion_config.train_data_path, index = False)
            test_data.to_csv(self.ingestion_config.test_data_path, index = False)

            logging.info("data ingestion part completed")


            return(

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            logging.info("Exception during occured at data ingestion stage")
            raise customerException(e,sys)