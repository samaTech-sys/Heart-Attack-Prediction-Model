#Importing dependencies 
from heartAttack.constants import *
from heartAttack.utils.common import read_yaml, create_directories
from heartAttack.entity.entity_config import (
    DataIngestionConfig, 
    DataValidationConfig, 
    DataProcessingConfig, 
    DataTransformationConfig,
    DataSplittingConfig,
    ModelTrainerConfig
    )

#Updating the configuration file 
class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH, 
        params_filepath = PARAMS_FILE_PATH,
        selected_schema_filepath = SELECTED_SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.selected_schema = read_yaml(selected_schema_filepath)
       
        create_directories([self.config.artifacts_root])
    
    #Step 1: Data Ingestion method 
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file, 
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    #Step 2: Data Validation method 
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir, 
            all_schema=schema
        )
        return data_validation_config
    
    #Step 3: Data Processing method 
    def get_data_processing_config(self) -> DataProcessingConfig:
        config = self.config.data_processing
        data_validation_config = self.config.data_validation
        selected_schema = self.selected_schema.COLUMNS  
            
        # Get target column from selected_schema 
        target_column = getattr(self.selected_schema, 'TARGET_COLUMN', None)
        if target_column is None:
            raise ValueError("Target column not specified in selected schema")
        
        create_directories([config.root_dir])
        
        data_processing_config = DataProcessingConfig(
            root_dir=Path(config.root_dir),
            validation_report= Path(config.validation_report),
            selected_data_file=Path(config.selected_data_file),
            all_schema=selected_schema,
            unzip_data_dir=Path(data_validation_config.unzip_data_dir),
            target_column=target_column  
        )
        return data_processing_config
    
    #Step 4: Data Transformation method 
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        data_processing_config = self.config.data_processing 
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            processed_data_file=Path(config.processed_data_file),
            selected_data_file=data_processing_config.selected_data_file,
        )
        return data_transformation_config
    
    #Step 5: Data Splitting method 
    def get_data_splitting_config(self) -> DataSplittingConfig:
        config = self.config.data_splitting
        data_transformation_config = self.config.data_transformation
        params = self.params.data_splitting
        
        create_directories([config.root_dir])
        
        data_splitting_config = DataSplittingConfig(
            root_dir=config.root_dir,
            processed_data_file=data_transformation_config.processed_data_file, 
            train_set_path=config.train_set_path, 
            test_set_path=config.test_set_path, 
            test_size=float(params.test_size),
            random_state=int(params.random_state)    
        )
        return data_splitting_config
    
     #Step 7: Model Training method 
    def get_model_training_config(self) -> ModelTrainerConfig:
        config = self.config.model_training
        params = self.params.ELASTICNET
        selected_schema = self.selected_schema.TARGET_COLUMN
        
        create_directories([config.root_dir])
        
        model_training_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name=config.model_name, 
            alpha= params.alpha,
            l1_ratio= params.l1_ratio,
            target_column=selected_schema.name
        )
        return model_training_config