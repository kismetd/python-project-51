[![Actions Status](https://github.com/kismetd/python-project-51/workflows/hexlet-check/badge.svg)](https://github.com/kismetd/python-project-51/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/3fddb3ecb7c169a9517f/maintainability)](https://codeclimate.com/github/kismetd/python-project-51/maintainability) [![codecov](https://codecov.io/gh/kismetd/python-project-51/branch/main/graph/badge.svg?token=J2N2AFRHN0)](https://codecov.io/gh/kismetd/python-project-51)

## page-loader: CLI utility to download web pages

[![asciicast](https://asciinema.org/a/jvzvnEIEpOmACuLLROb9sUrnn.svg)](https://asciinema.org/a/jvzvnEIEpOmACuLLROb9sUrnn)



## Installation:

### **with pip**:

```sh
$ pip install --user git+https://github.com/kismetd/python-project-51
```

### **with poetry** and **makefile**:

1. Get [poetry](https://python-poetry.org/).
2. Clone, move to directory with cloned repository.
3. `make install` or `poetry install`
4. `make build` or `poetry build`
5. `make install` or `python3 -m pip install --user --force-reinstall dist/*.whl`



## Usage:

### Import and use a library:

```python
from page_loader import download

file_path = download("https://ru.hexlet.io/courses", "/var/tmp")
print(file_path)  # /var/tmp/ru-hexlet-io-courses.html
```

### As a CLI application:

```sh
$ page-loader --help
usage: page-loader [options] <url>

Download web-pages and saves localy

positional arguments:
  url                   url to download

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to save the page content
  -l {debug,info,warning,error,critical}, --log {debug,info,warning,error,critical}
                        Set log level
```







