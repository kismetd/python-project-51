import os
from pathlib import Path

SEP = os.sep
URL = "https://ru.hexlet.io/courses"
TEST_FILE = "raw.html"


def get_fixture_path(file_name):
    return str(Path.cwd() / "tests" / "fixtures" / file_name)
