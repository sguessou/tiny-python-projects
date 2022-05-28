#!/usr/bin/env python3
"""
Author : sguessou <sguessou@localhost>
Date   : 2022-05-28
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", help="Output filename", metavar="str", type=str, default=""
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.isfile(args.text):
        file_handle = open(args.text, "r")
        print(file_handle.read().upper())
    else:
        print(args.text.upper())


# --------------------------------------------------
if __name__ == "__main__":
    main()
