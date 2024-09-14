from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import Evaluation
from cnnClassifier import logger



STAGE_NAME_04 = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__=="__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME_04} started <<<<")
        obj4 = ModelEvaluationPipeline()
        obj4.main()
        logger.info(f">>>> stage {STAGE_NAME_04} completed <<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
