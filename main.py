from heartAttack import logger 
from heartAttack.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from heartAttack.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from heartAttack.pipeline.stage_03_data_processing import DataProcessingTrainingPipeline
from heartAttack.pipeline.stage_04_data_transformation import DataTransformationTrainingPipeline
from heartAttack.pipeline.stage_05_data_splitting import DataSplittingTrainingPipeline
from heartAttack.pipeline.stage_06_model_training import ModelTrainingTrainingPipeline

#Step 1: Data Ingestion
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

#Step 2: Data Validation
STAGE_NAME = "Data Validataion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

#Step 3: Data Processing
STAGE_NAME = "Data Processing Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataProcessingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

#Step 4: Data Transformation
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

#Step 5: Data Splitting
STAGE_NAME = "Data Splitting Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataSplittingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)


#Step 6: Model Training 
STAGE_NAME = "Model training Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)



