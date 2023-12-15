import os
from pathlib import Path
import logging  # to log into about runtimes

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "textSummarizer"

# .gitkeep would be a hidden file simply to have something in the file
list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init_.py",  # constructor file - used for installing any local files as modules if need be
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/loggging/_init_.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init_.py",
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constants/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",  # Folder to run all our experiments
]

for filepath in list_files:
    filepath = Path(filepath)  # to convert the string to an actual path
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(
            filedir, exist_ok=True
        )  # Create directory if it doesn't exist already
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # just want to create a file and nothing else
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
