import os
import yaml
from box.exceptions import BoxValueError
from src.textSummarizer.logger import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError as box_exception:
        raise box_exception


