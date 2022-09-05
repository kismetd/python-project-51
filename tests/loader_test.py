from pathlib import Path
from urllib.parse import urljoin

import pytest
from page_loader.loader import download
from tests.conftest import LOCAL_DIR, LOCAL_PAGE, URL, get_fixture_path


@pytest.fixture
def html_empty():
    return "<html></html>"


def test_download_makes_expected_dir(requests_mock, html_empty, tmp_path):
    expected = html_empty
    requests_mock.get(URL, text=expected)
    _ = download(URL, tmp_path)

    assert Path(tmp_path, LOCAL_DIR).exists() is True


def test_download_gets_page_empty(requests_mock, html_empty, tmp_path):
    expected = html_empty
    requests_mock.get(URL, text=expected)
    _ = download(URL, tmp_path)

    assert Path(tmp_path, LOCAL_DIR, LOCAL_PAGE).exists() is True


@pytest.fixture
def page_with_resources(requests_mock):
    page_content = Path(get_fixture_path("remote_page.html")).read_text()
    requests_mock.get(URL, text=page_content)

    img_url = urljoin(URL, "/assets/professions/python.png")
    img_data = Path(get_fixture_path("image.png")).read_bytes()
    requests_mock.get(url=img_url, content=img_data)


def test_download_page_with_resources(page_with_resources, tmp_path):
    tempdir = Path(download(URL, tmp_path)).parent
    fixture_names = ("local_page.html", "image.png")
    fixtures = [Path(get_fixture_path(file)) for file in fixture_names]
    files = [Path(tempdir, file) for file in Path(tempdir).rglob("*")]

    actual = sorted(map(lambda x: x.stat().st_size, files))
    expected = sorted(map(lambda x: x.stat().st_size, fixtures))
    assert actual == expected
