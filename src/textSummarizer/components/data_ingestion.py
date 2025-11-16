import os
from pathlib import Path
import urllib.request as request
import zipfile
from src.textSummarizer.logger import logging
from src.textSummarizer.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        logging.info("Starting data download...")
        if not os.path.exists(self.config.local_data_file):
            os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
            filename, _ = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file)
            logging.info(f"Data downloaded successfully and saved to {filename}")
        else:
            logging.info("Data file already exists. Skipping download.")

    def extract_zip_file(self):
        logging.info("Starting data extraction...")
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logging.info(f"Data extracted successfully to {unzip_path}")
