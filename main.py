from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "DATA INGESTION"

try:

    logger.info(f">>>>>>> stag {STAGE_NAME} started <<<<<<<<<")
    dataingestio = DataIngestionTrainingPipeline()
    dataingestio.main()
    logger.info(f">>>>>>> stag {STAGE_NAME} completed <<<<<<<<<")

except Exception as e:

    logger.exception(e)
    raise e