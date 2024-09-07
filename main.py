# this is the  entry point
from cnnClassifier import logger # as cnnclassifier is setup as local package through setup.py
from cnnClassifier.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline, STAGE_NAME

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e