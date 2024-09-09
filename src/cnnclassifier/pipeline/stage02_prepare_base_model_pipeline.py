from cnnClassifier.config.configuration import ConfiguratonManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME_02 = "Prepare Base Model stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguratonManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        

if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME_02} started <<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME_02} completed <<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e