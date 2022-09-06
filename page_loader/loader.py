"""Download web pages locally"""
import logging
from pathlib import Path

import page_loader.exceptions as exceptions
import requests
from bs4 import BeautifulSoup
from page_loader.htmlutils import get_sources_and_update
from page_loader.urlutils import url_to_filename

DEFAULT_DIR = str(Path.cwd())
logger = logging.getLogger(__name__)


def _make_request(url: str) -> requests.Response:
    return requests.get(url)


@exceptions.filesystem_err
@exceptions.makedir_handler
def download(url: str, dir=DEFAULT_DIR) -> str:
    """Download html page and save in given existing directory.

    Args:
        url (str): url to a web page
        dir (str): existing directory path

    Returns:
        str: full path to saved file
    """
    dir_name = url_to_filename(url, "_files")
    dir_path = Path(dir, dir_name)
    Path.mkdir(dir_path)

    page_name = url_to_filename(url, ".html")
    page_path = Path(dir_path, page_name)
    page_data = _make_request(url).content
    parsed_page = BeautifulSoup(page_data, "html.parser").prettify()
    Path(page_path).write_text(parsed_page)

    sources = get_sources_and_update(str(page_path), dir_name, url)
    for abs_url, local_name in sources.items():
        file_path = str(Path(dir, local_name))
        if Path(file_path).exists():
            continue
        file_data = _make_request(abs_url).content
        Path(file_path).write_bytes(file_data)

    return str(page_path)
