from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngesion
from cnnClassifier import logger

STAGE_NAME_01 = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngesion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        

if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME_01} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME_01} completed <<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e