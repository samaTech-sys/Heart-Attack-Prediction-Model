import os
from urllib import request
from pathlib import Path 
import zipfile
from heartAttack import logger
from heartAttack.utils.common import get_size
from heartAttack.entity.entity_config import DataIngestionConfig

#Unpdate Components step
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, 
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with the following info: n\{headers}")
        else: 
            logger.info(f"File already exists: {get_size(Path(self.config.local_data_file))}")
        print("Downloding", self.config.source_url)
            
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts zip file into directory 
        Function returne none
        
        """
        
        unzip_path = self.config.unzip_dir
        # Print the actual path of the local data file and unzip directory
        print(f"Extracting file from: {self.config.local_data_file}")
        print(f"Unzip path: {unzip_path}")

        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)