from pathlib import Path
import pandas as pd
import json
from typing import Any, Dict
from .paths import get_data_dir

class DataHandler:
    """Handles data operations across the project."""
    
    @staticmethod
    def get_data_path(filename: str) -> Path:
        """Get full path for a file in the data directory."""
        return get_data_dir() / filename
    
    @classmethod
    def load_csv(cls, filename: str) -> pd.DataFrame:
        """Load a CSV file from the data directory."""
        file_path = cls.get_data_path(filename)
        return pd.read_csv(file_path)
    
    @classmethod
    def save_csv(cls, df: pd.DataFrame, filename: str) -> None:
        """Save a DataFrame to CSV in the data directory."""
        file_path = cls.get_data_path(filename)
        df.to_csv(file_path, index=False)
    
    @classmethod
    def load_json(cls, filename: str) -> Dict[str, Any]:
        """Load a JSON file from the data directory."""
        file_path = cls.get_data_path(filename)
        with open(file_path, 'r') as f:
            return json.load(f)
    
    @classmethod
    def save_json(cls, data: Dict[str, Any], filename: str) -> None:
        """Save data to JSON in the data directory."""
        file_path = cls.get_data_path(filename)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)