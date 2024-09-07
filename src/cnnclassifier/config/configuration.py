from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig


class ConfiguraitonManager:
    def __init__(
            self, 
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH
        ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig: #define return type of this function
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig( #assign return type of this function
            #reading all the config one by one  store the value in these variables
            root_dir=config.root_dir,
            souce_URL= config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        # thats how we write custom return type of the function  using entity which can be esily use that in my component
        return data_ingestion_config


