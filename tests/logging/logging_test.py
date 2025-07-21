from pathlib import Path
import logging  # standard Python logging module
from sinthia.core import logging as sinthia_logging  # your custom module
import pytest

sinthia_logging.init_logging()  # Initialize logging configuration
logging_dir = Path(sinthia_logging.__file__).parent

def test_logging_module_files_exist():
    expected_files = ["config.json", "myLogger.py", "__init__.py"]
    for filename in expected_files:
        file_path = logging_dir / filename
        assert file_path.exists(), f"Missing expected file: {file_path}"


def test_loggers_exist() -> None:
    """Test that all loggers are defined in the logging configuration."""
    expected_loggers = [
        "sinthia",
        "sinthia.transcription",
        "sinthia.tts",
        "sinthia.restAPI",
        "sinthia.report"
    ]
    for logger_name in expected_loggers:
        logger = logging.getLogger(logger_name)
        assert logger is not None, f"Logger {logger_name} does not exist"
        assert logger.hasHandlers(), f"Logger {logger_name} has no handlers"
        assert logger.level != logging.NOTSET, f"Logger {logger_name} has NOTSET level"
