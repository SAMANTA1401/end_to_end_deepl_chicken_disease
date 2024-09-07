import os
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


#create data ingestion component
class DataIngesion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.souce_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} has been downloaded ! with folowing info: \n{headers}")
        else:
            logger.info(f"file already exists of size: {get_size(path=self.config.local_data_file)}")
        
    def extract_zip_file(self):
        """
        extract zip file to local data directory
        zip_file_path :str
        function return None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"zip file has been extracted successfully")

