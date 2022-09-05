from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from page_loader.htmlutils import get_sources_and_update
from tests.conftest import URL, get_fixture_path


@pytest.mark.parametrize(
    "remote, local, dir",
    [
        ("remote_page.html", "local_page.html", "ru-hexlet-io-courses_files"),
    ],
)
def test_get_sources_and_update_changes_tags_correctly(remote, local, dir):
    remote, expected = get_fixture_path(remote), get_fixture_path(local)
    expected = Path(expected).read_text()

    with TemporaryDirectory() as tmpdir:
        temp_path = str(Path(tmpdir, "actual"))
        text_before = Path(remote).read_text()
        with open(temp_path, "w") as page:
            page.write(text_before)

        _ = get_sources_and_update(temp_path, dir, URL)
        actual = Path(temp_path).read_text()

        assert actual == expected
