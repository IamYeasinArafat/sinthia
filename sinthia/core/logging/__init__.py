# __init__.py
import logging
import logging.config
from pathlib import Path
import json

def init_logging():
    if logging.getLogger().hasHandlers():
        return  # logging already configured

    config_path = Path(__file__).parent / "config.json"
    with open(config_path, "r") as f:
        config = json.load(f)
    logging.config.dictConfig(config)


__all__ = ["init_logging"]