import argparse

from page_loader import logconf
from page_loader.loader import DEFAULT_DIR


def get_args():
    parser = argparse.ArgumentParser(
        prog="page-loader",
        description="Download web-pages and saves localy",
        usage="page-loader [options] <url>",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to save the page content",
        default=DEFAULT_DIR,
        type=str,
    )
    parser.add_argument(
        "url",
        help="url to download",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--log",
        help="Set log level",
        default="WARNING",
        choices=logconf.CONFIGS.keys(),
    )
    args = parser.parse_args()
    return args.output, args.url, args.log
