from pathlib import Path

URL = "https://ru.hexlet.io/courses"
LOCAL_DIR = "ru-hexlet-io-courses_files"
LOCAL_PAGE = "ru-hexlet-io-courses.html"


def get_fixture_path(file_name):
    return str(Path.cwd() / "tests" / "fixtures" / file_name)
