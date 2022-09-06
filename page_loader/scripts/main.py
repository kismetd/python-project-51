#!/usr/bin/env python3
"""
Download web pages locally
"""
import logging

from page_loader.cli import get_args
from page_loader.exceptions import FileSystemError, NetworkError
from page_loader.loader import download
from page_loader.logconf import setup

logger = logging.getLogger(__name__)


def main():
    target_dir, url, log_lvl = get_args()
    setup(log_lvl)
    try:
        print(download(url, target_dir))
    except (NetworkError, FileSystemError):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
