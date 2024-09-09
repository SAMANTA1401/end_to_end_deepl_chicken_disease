# this is the  entry point
from cnnClassifier import logger # as cnnclassifier is setup as local package through setup.py
from cnnClassifier.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline, STAGE_NAME_01
from cnnClassifier.pipeline.stage02_prepare_base_model_pipeline import PrepareBaseModelPipeline , STAGE_NAME_02

try:
    # stage 01 data ingestion
    logger.info(f">>>> stage {STAGE_NAME_01} started <<<<")
    obj1 = DataIngestionTrainingPipeline()
    obj1.main()
    logger.info(f">>>> stage {STAGE_NAME_01} completed <<<<<<\n\nx=======x")

    # stage 02 prepare base model
    logger.info(f">>>> stage {STAGE_NAME_02} started <<<<")
    obj2 = PrepareBaseModelPipeline()
    obj2.main()
    logger.info(f">>>> stage {STAGE_NAME_02} completed <<<<<<\n\nx=======x")


except Exception as e:
    logger.exception(e)
    raise e