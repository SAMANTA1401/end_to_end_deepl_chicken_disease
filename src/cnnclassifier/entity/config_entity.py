from dataclasses import dataclass
from pathlib import Path


#entities entities class name for dataingesion compoenent
@dataclass(frozen=True)
class DataIngestionConfig: # this is actually not a python class it is a dataclass which define return type of a python function
    root_dir: Path
    souce_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path