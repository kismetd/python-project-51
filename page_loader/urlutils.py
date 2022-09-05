"""Utility functions to work with url paths"""
import os
import re
from urllib.parse import urlparse


def _format(text: str):
    return re.sub(r"[^\w\s]", "-", text)


def url_to_filename(url: str, ext="") -> str:
    url_parts = urlparse(url)
    netloc = url_parts.netloc
    path, extension = os.path.splitext(url_parts.path)

    if ext:
        extension = ext

    filename = _format("".join([netloc, path]))
    return f"{filename}{extension}"


def is_local(url: str, src: str) -> bool:
    if not urlparse(src).netloc:
        return True
    return urlparse(url).netloc == urlparse(src).netloc
