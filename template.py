import os 
from pathlib import Path 
import logging

#logging string 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name ='heartAttack'

#List of files and folders 
list_of_files = [
    ".github/workflows/.gitkeep", 
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml", 
    "dvc.yaml", 
    "params.yaml", 
    "schema.yaml", 
    "selected_schema.yaml",
    "requirements.txt",
    "setup.py", 
    "docs",
    "research/trials.ipynb", 
    "reports/",
    "analysis/steps/step1_basic_data_inspection.py", 
    "engineering/styles/style1_handle_missing_values.py", 
    "templates/index.html", 
    "main.py"
]

for filepath in list_of_files: 
    filepath =Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty path: {filepath}")
        
    else: 
        logging.info(f"{filename} already exists")
        