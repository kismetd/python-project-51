import argparse
import os

from page_loader import download

parser = argparse.ArgumentParser(
    description="Download a web page and save it locally",
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    default=os.getcwd,
    help="path to save the page content",
)
parser.add_argument("url", type=str, help="url address")
args = parser.parse_args()


def main():
    print(download(args.url, args.output))


if __name__ == "__main__":
    main()
