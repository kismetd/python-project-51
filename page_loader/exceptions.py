import functools
import logging

logger = logging.getLogger(__name__)


class FileSystemError(Exception):
    pass


class NetworkError(Exception):
    pass


def filesystem_err(func):
    """Safe work with filesystem"""

    @functools.wraps(func)
    def wrapper_filesystem_err(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except FileExistsError as e:
            logger.error(
                msg=(
                    "Failed to make new directory. Proceeding to write files under the same path."  # noqa E501
                ),
                exc_info=e,
            )

        except FileNotFoundError as e:
            logger.error(
                msg=("File not found."),  # noqa E501
                exc_info=e,
            )
            raise FileSystemError from e

        except OSError as e:
            logger.error(e)
            raise FileSystemError from e

    return wrapper_filesystem_err
