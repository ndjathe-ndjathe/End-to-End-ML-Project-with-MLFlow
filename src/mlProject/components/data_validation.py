import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataValidation:
    config: DataValidationConfig

    def validate_all_columns(self) -> bool:
        logger.info(f"Validating data")
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            logger.info(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            logger.exception(f"Exception while validating data : \n{e}")
            raise e

