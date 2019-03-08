"""Parsing of CLI input (args)."""

import argparse
from ickinesis.__version__ import VERSION


def get_args():
    """Parse args"""

    parser = argparse.ArgumentParser(description="Get records from kinesis")
    parser.add_argument("-s", "--stream", help="kinesis stream")
    parser.add_argument("--capture", dest="capture", action="store_true")
    parser.add_argument("--no-color", dest="no_color", action="store_true")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=VERSION,
        help="ickinesis version",
        default=None,
    )
    return parser.parse_args()
