import pytest
from page_loader.urlutils import is_local, url_to_filename


@pytest.mark.parametrize(
    "url, ext, expected",
    [
        pytest.param(
            "https://ru.hexlet.io/courses",
            "",
            "ru-hexlet-io-courses",
            id="simple url",
        ),
        pytest.param(
            "https://ru.hexlet.io/courses.html",
            "",
            "ru-hexlet-io-courses.html",
            id="url ends with .html, no extension arg",
        ),
        pytest.param(
            "assets/application.css",
            "",
            "assets-application.css",
            id="no netloc, extension in url, no extension arg",
        ),
        pytest.param(
            "https://ru.hexlet.io/courses",
            "_files",
            "ru-hexlet-io-courses_files",
            id="extension arg specified",
        ),
    ],
)
def test_url_to_filename(url, ext, expected):
    assert url_to_filename(url, ext) == expected


@pytest.mark.parametrize(
    "full_url, src, expected",
    [
        (
            "https://ru.hexlet.io/courses",
            "assets/professions/python.png",
            True,
        ),
        (
            "https://ru.hexlet.io/courses",
            "https://ru.hexlet.io/assets/professions/python.png",
            True,
        ),
        (
            "https://ru.hexlet.io/courses",
            "https://cdn2.hexlet.io/assets/menu.css",
            False,
        ),
    ],
)
def test_is_local(full_url, src, expected):
    assert is_local(full_url, src) == expected
