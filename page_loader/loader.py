"""Download web pages locally"""
import os
import re

import requests


def _format_path(url: str, dir: str) -> str:
    address = url.split("://")[1]
    file_name = re.sub(r"[^\w\s]", "-", address) + ".html"
    return os.path.join(dir, file_name)


def download(url: str, dir=os.getcwd()) -> str:
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
