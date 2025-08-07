import os
from box.exceptions import BoxValueError
import yaml
from wine_quality_prediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns
    
    Args:
        path_to_yaml (str): Path like input
        
    Raises:
        ValueError: If the YAML file is empty
        e: empty file 

    Returns:
        ConfigBox: ConfixBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"YAML file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose= True):
    """
    Creates list of directories
    
    Args:
        path_to_directories (list): List of directory paths to create
        ignore_log (bool, optional): ignore if multiple directories are created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> dict:
    """
    Loads a dictionary from a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        dict: Data loaded from the JSON file.
    """
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file loaded from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Saves data to a binary file
    
    Args:
        path (Path): Path to the binary file.
        data (Any): Data to be saved.
    """
    joblib.dump(value = data, filename= path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(filename= path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> int:
    """
    Returns the size of a file or directory.
    
    Args:
        path (Path): Path to the file or directory.
        
    Returns:
        int: Size in bytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB" if size_in_kb > 0 else "0 KB"