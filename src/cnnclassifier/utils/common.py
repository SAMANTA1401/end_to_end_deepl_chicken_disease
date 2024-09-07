import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations # this decorator handle wrong input datatype  2*"3" =222 unfortunatelt actulally i want 2*3=6 this decorator inform about the error
def read_yaml(path_to_yaml:Path) ->ConfigBox:  # config box allow to return value from a dict as dict.key format rather than dict['key'] format
    """
        Read a YAML file and convert it into a ConfigBox object.

        Args:
        path_to_yaml (Path): Path to the YAML file.

        Raises:
        BoxValueError: If the YAML file is not valid.
        e: empty file

        Returns:
        ConfigBox: ConfigBox object containing the YAML data. 
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loadded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


    
@ensure_annotations
def save_json(path:Path,data:dict):
    """
    Save a dictionary into a JSON file.
    path : path to json file

    data : data to be saved in json file 
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at : {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file into a ConfigBox object.
    path : path to json file
    Args:
    path: path to json file
    Returns:
    ConfigBox: ConfigBox object containing the JSON data.

    """
    with open(path, 'r') as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    '''
    Save binary data to a file.
    data : data to be saved
    path : path to save the data
    '''
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    '''
    Load binary data from a file.
    path : path to the binary file
    Returns:
    Any: object stored in the file
    '''
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded  from: {path}")
    return data
    
    
@ensure_annotations
def get_size(path: Path) -> str:
    '''
    Get the size of a file in kb.
    path : path to the file
    Returns:
    str: size of the file in k bytes
    '''
    size = os.path.getsize(path)
    return "size is " + str(size / 1024) + " KB"         
    

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        img_content = f.read()
        return base64.b64encode(img_content)
    

