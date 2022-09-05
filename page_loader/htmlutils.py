"""Utility functions to work with html files"""
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from page_loader.urlutils import is_local, url_to_filename

_TAGS = ("img", "link", "script")

_ATTRIBUTES = {
    "img": "src",
    "link": "href",
    "script": "src",
}


def get_sources_and_update(html: str, dir: str, url: str) -> dict[str, str]:
    """Finds all local resources in a html page.

    A resource is called local if its 'src' or 'href' attribute
    points to the same domain (Network location part) as the
    html-page it is part of.

    Returns URLs of all local resources in the document and
    paths to their copies on the machine.

    Args:
        html (str): Path to html file.
        dir (str): Path to directory where resources will be stored.
        url (str): Url to given html page

    Returns:
        dict[str, str]: Key: URLs of all local resources. Value: paths to
        them on the computer.
    """
    paths = {}
    data = Path(html).read_text()
    page = BeautifulSoup(data, "html.parser")
    tags = page.find_all("img")  # only for images for now

    for tag in tags:
        attr = _ATTRIBUTES[tag.name]
        source = tag.get(attr)
        if is_local(url, source):
            abs_src = urljoin(url, source)
            local_file = url_to_filename(abs_src)
            local_path = str(Path(dir, local_file))
            paths[abs_src] = local_path
            tag[attr] = str(Path(local_path))

    updated = page.prettify()
    Path(html).write_text(updated)

    return paths
