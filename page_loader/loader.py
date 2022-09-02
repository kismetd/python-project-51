"""Download web pages locally"""
import re
from pathlib import Path

import requests


def _format_path(url: str, dir: str) -> str:
    address = url.split("://")[1]
    suffix = Path(address).suffix
    if suffix == ".html":
        address = address[: -len(suffix)]
    address = re.sub(r"[^\w\s]", "-", address)
    filename = ".".join([address, "html"])
    return str(Path(dir, filename))


def download(url: str, dir: str) -> str:
    """Download html page and save in given existing directory.

    Args:
        url (str): url to a web page
        dir (str): existing directory path

    Returns:
        str: full path to saved file
    """
    response = requests.get(url)
    save_path = _format_path(url, dir)
    with open(save_path, "w") as f:
        f.write(response.text)
    return save_path
