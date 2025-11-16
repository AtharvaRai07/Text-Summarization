from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.logger import logging

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logging.info(f"Initiated : -----------------{STAGE_NAME}-----------------")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logging.info(f"Completed : -----------------{STAGE_NAME}-----------------")
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "DATA TRANSFORMATION STAGE"

try:
    logging.info(f"Initiated : -----------------{STAGE_NAME}-----------------")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initaite_data_transformation()
    logging.info(f"Completed : -----------------{STAGE_NAME}-----------------")
except Exception as e:
    logging.exception(e)
    raise e

