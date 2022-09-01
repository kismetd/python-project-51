import tempfile
from pathlib import Path

import requests_mock
from page_loader.loader import download

URL = "https://ru.hexlet.io/courses"
TEST_FILE = "raw.html"


def get_fixture_path(file_name):
    return str(Path.cwd() / "tests" / "fixtures" / file_name)


def test_download_makes_request_and_saves_file():
    fixture_path = get_fixture_path(TEST_FILE)
    expected = Path(fixture_path).read_bytes()
    with requests_mock.Mocker() as m:
        m.get(URL, content=expected)
        with tempfile.TemporaryDirectory() as tmpdir:
            result_path = download(URL, tmpdir)
            result = Path(result_path).read_bytes()

    assert result == expected
