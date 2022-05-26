#!/usr/bin/env python3
"""
Author : sguessou <sguessou@localhost>
Date   : 2022-05-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("item", metavar="str", nargs="+", help="Item(s) to bring")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item

    if len(items) > 1 and args.sorted:
        items.sort()

    if len(items) == 1:
        print(f"You are bringing {items[0]}.")
    elif len(items) == 2:
        print(f"You are bringing {items[0]} and {items[1]}.")
    else:
        items[-1] = "and " + items[-1]
        bringing = ", ".join(items)
        print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
