from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.model_training import Training

STAGE_NAME_03 = 'Model Training Stage'



class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        #callback pipeline
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        #training pipeline
        Training_config = config.get_training_config()
        training = Training(config=Training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list = callback_list
        )


if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME_03} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME_03} completed <<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e