import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')



project_name = "cnnclassifier"

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    'research/trials.ipynb',
    'templates/index.html'

]

for filepath in list_of_file:
    filepath = Path(filepath) # we created this file with forward / (linux) but actualy windows uses backward \ so path class converted
    #this linux path to windows path

    filedir , filename = os.path.split(filepath) #splitted by /

    if filedir !="":
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f"Creating directory; {filedir} for the filename: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists;")