import os 
import pandas as pd 
import numpy as np
from pathlib import Path 
from heartAttack import logger
from heartAttack.entity.entity_config import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.df = pd.read_csv(self.config.selected_data_file)
        self.processed_df = None
    

    def process_and_store_data(self) -> None:
        """
        Execute full processing pipeline and store results
        Args:
            df: Raw input DataFrame
        """
        df=self.df.copy() #work on a copy of dataframe
        df = self.fill_missing_with_mode(df)  # Step 2: Handle missing values: Example to all call classes tranforming data here
        self.processed_df = df # Store processed data
        
        # Save to artifacts
        os.makedirs(self.config.root_dir, exist_ok=True)
        save_path = Path(self.config.root_dir) / "processed_df.csv"
        df.to_csv(save_path, index=False)
        logger.info(f"Processed data stored at: {save_path}")
    
    def fill_missing_with_mode(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fill missing values in each column with the column's mode.
        """
        for col in df.columns:
            if df[col].isnull().any():
                try:
                    mode_val = df[col].mode()[0]
                    df[col].fillna(mode_val, inplace=True)
                except Exception as e:
                    logger.warning(f"Could not fill missing values in column '{col}': {e}")
        return df