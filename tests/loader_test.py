import tempfile
from pathlib import Path

import pytest
import requests_mock
from conftest import SEP, TEST_FILE, URL, get_fixture_path

from page_loader.loader import download


def test_download_makes_request_and_saves_file():
    fixture_path = get_fixture_path(TEST_FILE)
    expected = Path(fixture_path).read_bytes()
    with requests_mock.Mocker() as m:
        m.get(URL, content=expected)
        with tempfile.TemporaryDirectory() as tmpdir:
            result_path = download(URL, tmpdir)
            result = Path(result_path).read_bytes()

    assert result == expected


@pytest.mark.parametrize(
    "url, expected",
    [
        (
            "https://ru.hexlet.io/courses",
            "ru-hexlet-io-courses.html",
        ),
        (
            "https://ru.hexlet.io/courses.html",
            "ru-hexlet-io-courses.html",
        ),
    ],
)
def test_download_saves_with_correct_names(url, expected):
    fixture_path = get_fixture_path(TEST_FILE)
    cont = Path(fixture_path).read_bytes()
    with requests_mock.Mocker() as m:
        m.get(url, content=cont)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = download(url, tmpdir)
            filename = path.split(SEP)[-1]

    assert filename == expected
