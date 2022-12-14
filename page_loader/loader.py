"""Download web pages locally"""
import logging
from pathlib import Path

import page_loader.exceptions as exceptions
import requests
from page_loader.htmlutils import get_sources_and_update
from page_loader.urlutils import url_to_filename
from progress.bar import ChargingBar

DEFAULT_DIR = str(Path.cwd())
logger = logging.getLogger(__name__)


def _get_content(url: str):
    response = requests.request("GET", url)
    response.raise_for_status()
    logger.info(f"Fetching content from {url}... Success!")

    return response.content


@exceptions.filesystem_err
def _load_resources(sources: dict[str, str], dir: str) -> None:
    """Attempt to load all local resources. Doesn't terminate on failure."""
    with ChargingBar("Downloading", max=len(sources)) as bar:
        for abs_url, local_name in sources.items():
            file_path = str(Path(dir, local_name))
            if Path(file_path).exists():
                logger.info(f"{file_path} already exists! Skipping...")
                continue

            try:
                file_data = _get_content(abs_url)
                Path(file_path).write_bytes(file_data)
                logger.info(f"Saving {file_path}... Success!")
                bar.next()
            except requests.exceptions.RequestException as e:
                logger.debug(msg="Network Error", exc_info=e)
                logger.warning(f"Failed fetch file: {abs_url}. Skipping...")


@exceptions.filesystem_err
def download(url: str, dir=DEFAULT_DIR) -> str:
    """Download html page and save in given existing directory.

    Args:
        url (str): url to a web page
        dir (str): existing directory path

    Returns:
        str: full path to saved file
    """

    page_name = url_to_filename(url, ".html")
    page_path = Path(dir, page_name)

    try:
        page_data = _get_content(url)
        logging.info(f"Getting page: {url}... Success!")
    except requests.exceptions.RequestException as e:
        logger.debug(msg="Network Error", exc_info=e)
        logger.warning(f"Failed fetch page: {url}.")
        logger.warning("Cannot proceed without html document! Terminating...")
        raise exceptions.NetworkError from e

    Path(page_path).write_bytes(page_data)
    logger.info(f"Saving page {url}... Success!")

    dir_name = url_to_filename(url, "_files")
    sources = get_sources_and_update(str(page_path), dir_name, url)
    if sources:
        dir_path = Path(dir, dir_name)
        Path.mkdir(dir_path)
        logger.info("Expected to load page resources.")
        logger.info(f"Directory '{dir_path}' was created.")
        _load_resources(sources, dir)

    return str(page_path)
