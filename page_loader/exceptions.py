import functools
import logging

logger = logging.getLogger(__name__)


def makedir_handler(func):
    """Safe work with filesystem"""

    @functools.wraps(func)
    def wrapper_safe_makedir(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            logger.error("Unable to find existing directory", exc_info=e)
            raise SystemExit(e)
        except FileExistsError as e:
            logger.error(
                msg=(
                    "Failed to make new directory. Proceeding to write files under the same path."  # noqa E501
                ),
                exc_info=e,
            )
        except OSError as e:
            logger.error(e)
            raise SystemExit(e)

    return wrapper_safe_makedir


def filesystem_err(func):
    @functools.wraps(func)
    def wrapper_filesystem_err(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OSError as e:
            logger.error(e)
            raise SystemExit(e)

    return wrapper_filesystem_err
