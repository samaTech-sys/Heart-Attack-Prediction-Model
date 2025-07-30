from dataclasses import dataclass
from pathlib import Path

#Step 1: Data Ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path 
    unzip_dir: Path  
     
#Step 1: Data Validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path 
    all_schema: dict

#Step 3: Data Processing
@dataclass(frozen=True)
class DataProcessingConfig:
    root_dir: Path
    unzip_data_dir: Path
    selected_data_file: Path 
    validation_report: Path
    all_schema: dict
    target_column: str

#Step 4: Data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    selected_data_file: Path
    processed_data_file: Path

#Step 5: Data Splitting
@dataclass(frozen=True)
class DataSplittingConfig:
    root_dir: Path
    processed_data_file: Path
    train_set_path: Path
    test_set_path: Path
    test_size: float
    random_state: int

#Step 6: Model Training
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path 
    model_name: str 
    alpha: float
    l1_ratio: float
    target_column: str

#Step 7: Model Evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path 
    model_path: Path 
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str