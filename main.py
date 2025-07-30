from heartAttack import logger 
from heartAttack.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from heartAttack.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from heartAttack.pipeline.stage_03_data_processing import DataProcessingTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Validataion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)



STAGE_NAME = "Data Processing Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataProcessingTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed >>>>>\n\nx=========x")
except Exception as e:
    logger.exception(e)
