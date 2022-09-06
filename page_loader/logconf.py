"""Use to set logging configuration"""
import logging
import os

_LOGS_DIR = os.path.join(os.getcwd(), "logs")
if not os.path.exists(_LOGS_DIR):
    os.mkdir(_LOGS_DIR)

CONFIGS = {
    "debug": {
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "level": "DEBUG",
        "handlers": [
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(_LOGS_DIR, "page_loader.log")),
        ],
    },
    "info": {
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "level": "INFO",
        "handlers": [
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(_LOGS_DIR, "page_loader.log")),
        ],
    },
    "warning": {
        "format": "%(asctime)s - %(levelname)s - %(message)s",
        "level": "WARNING",
        "handlers": [
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(_LOGS_DIR, "page_loader.log")),
        ],
    },
    "error": {
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "level": "ERROR",
        "handlers": [
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(_LOGS_DIR, "page_loader.log")),
        ],
    },
    "critical": {
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "level": "CRITICAL",
        "handlers": [
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(_LOGS_DIR, "page_loader.log")),
        ],
    },
}


def setup(level="warning") -> None:
    """import inside an entry point module to set Logging Configuration.
    Logging levels in order of severity: DEBUG, INFO, WARNING, ERROR, CRITICAL.

    For example, if severity is set to the lowest level DEBUG:
    records all possible events from DEBUG up to CRITICAL level of severity.
    If set to WARNING: records only WARNING, ERROR and CRITICAL
    level events, an so on.


    Args:
        level (str): Logging level in lowercase
    """
    logging.basicConfig(
        level=CONFIGS[level]["level"],
        format=CONFIGS[level]["format"],
        handlers=CONFIGS[level]["handlers"],
    )
