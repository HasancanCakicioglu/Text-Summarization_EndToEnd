import os
from pathlib import Path
import logging

# Logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project Name
project_name = "textSummarizer"

# Path to the project directory
list_of_files = [
    ".github/workflows/.gitkeep", # Github Actions CI/CD
    f"src/{project_name}/__init__.py",  # Initializes the project package
    f"src/{project_name}/conponents/__init__.py",  # Initializes the components module
    f"src/{project_name}/utils/__init__.py",  # Initializes the utils module
    f"src/{project_name}/utils/common.py",  # Contains common utility functions
    f"src/{project_name}/logging/__init__.py",  # Initializes the logging module
    f"src/{project_name}/config/__init__.py",  # Initializes the configuration module
    f"src/{project_name}/config/configuration.py",  # Contains project-specific configuration settings
    f"src/{project_name}/pipeline/__init__.py",  # Initializes the pipeline module
    f"src/{project_name}/entity/__init__.py",  # Initializes the entity module
    f"src/{project_name}/constants/__init__.py",  # Initializes the constants module
    "config/config.yaml",  # Configuration file in YAML format
    "params.yaml",  # Parameters file in YAML format
    "app.py",  # Main application file
    "main.py",  # Entry point for the application
    "Dockerfile",  # Dockerfile for containerization
    "requirements.txt",  # Contains the required Python dependencies
    "setup.py",  # File for defining project metadata and dependencies
    "research/trials.ipynb"  # Jupyter Notebook file for research and experimentation
]


# Create pages
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Created empty file: {filepath}")
    
    else:
        logging.info(f"File already exists: {filename}")
            