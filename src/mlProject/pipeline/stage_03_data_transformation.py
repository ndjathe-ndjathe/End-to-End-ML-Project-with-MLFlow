from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from dataclasses import dataclass
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"

@dataclass
class DataTransformationTrainingPipeline:
    def main(self):

        config = ConfigurationManager()

        try:
            with open(Path(config.get_data_validation_config().STATUS_FILE)) as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e