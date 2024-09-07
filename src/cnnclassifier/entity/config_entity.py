from dataclasses import dataclass
from pathlib import Path


#entities entities class name for dataingesion compoenent
@dataclass(frozen=True)
class DataIngestionConfig: # this is actually not a python class it is a dataclass which define return type of a python function
    root_dir: Path
    souce_URL: str
    local_data_file: Path
    unzip_dir: Path