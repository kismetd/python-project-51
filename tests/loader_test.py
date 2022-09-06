import os
from pathlib import Path
from urllib.parse import urljoin

import pytest
import requests
from page_loader.loader import download
from tests.conftest import LOCAL_DIR, LOCAL_PAGE, URL, get_fixture_path


@pytest.fixture
def html_empty():
    return "<html></html>"


def test_download_page_empty(requests_mock, html_empty, tmp_path):
    expected = html_empty
    requests_mock.get(URL, text=expected)

    assert not Path(tmp_path, LOCAL_DIR).exists()
    download(URL, tmp_path)

    assert not Path(tmp_path, LOCAL_DIR).exists()
    assert Path(tmp_path, LOCAL_PAGE).exists()


@pytest.fixture
def page_with_resources(requests_mock):
    page_content = Path(get_fixture_path("remote_page.html")).read_text()
    requests_mock.get(URL, text=page_content)

    img_url = urljoin(URL, "/assets/professions/python.png")
    img_data = Path(get_fixture_path("image.png")).read_bytes()
    requests_mock.get(url=img_url, content=img_data)

    css_url = urljoin(URL, "/assets/application.css")
    css = Path(get_fixture_path("style.css")).read_bytes()
    requests_mock.get(url=css_url, content=css)

    script_url = urljoin(URL, "/packs/js/runtime.js")
    script = Path(get_fixture_path("script.js")).read_bytes()
    requests_mock.get(url=script_url, content=script)


def test_download_page_with_resources(page_with_resources, tmp_path):
    download(URL, tmp_path)
    tempdir = Path(tmp_path, LOCAL_DIR)
    fixture_names = ("remote_page.html", "image.png", "style.css", "script.js")
    fixtures = [Path(get_fixture_path(file)) for file in fixture_names]
    files = [Path(tempdir, file) for file in Path(tempdir).glob("*")]

    actual = sorted(map(lambda x: x.stat().st_size, files))
    expected = sorted(map(lambda x: x.stat().st_size, fixtures))
    assert actual == expected


def test_connection_error(requests_mock, tmp_path):
    invalid_url = "https://badsite.com"
    requests_mock.get(invalid_url, exc=requests.exceptions.ConnectionError)

    assert not os.listdir(tmp_path)

    with pytest.raises(Exception):
        assert download(invalid_url, tmp_path)

    assert not os.listdir(tmp_path)
