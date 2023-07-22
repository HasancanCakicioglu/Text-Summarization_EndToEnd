from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Running stage: {STAGE_NAME}")
    training_pipeline = DataIngestionTrainingPipeline()
    training_pipeline.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully!")
except Exception as e:
    logger.error(f"Stage: {STAGE_NAME} failed! Exception: {e}")
    raise e