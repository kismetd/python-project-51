from pathlib import Path

import pytest
from page_loader.exceptions import FileSystemError, NetworkError
from page_loader.loader import download
from tests.conftest import URL


def test_download_in_wrong_target_directory(tmp_path, requests_mock):
    non_existent_path = str(Path(tmp_path, "legit_dir"))
    requests_mock.get(URL)
    with pytest.raises(FileSystemError):
        _ = download(URL, non_existent_path)


def test_download_request_fails(tmp_path, requests_mock):
    requests_mock.get(URL, status_code=404)
    with pytest.raises(NetworkError):
        download(URL, tmp_path)
