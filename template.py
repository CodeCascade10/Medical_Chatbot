import os
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

# Project file structure
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent

    # Create directory if not exists
    if filedir != Path("."):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    # Create empty file if not exists
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")