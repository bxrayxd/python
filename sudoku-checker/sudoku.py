"""Sudoku solver with optional displays"""

import argparse
import display as sudoko_display
import reader

import logging

# set up logger
for handler in logging.root.handlers[:]:  # make sure all handlers are removed
    logging.root.removeHandler(handler)

logging_level = logging.DEBUG
logging_format = logging.Formatter(
    "%(asctime)s: %(levelname)s [%(name)s:%(funcName)s:%(lineno)d] - %(message)s"
)
logging.root.setLevel(logging_level)
h = logging.StreamHandler()
h.setFormatter(logging_format)
logging.root.addHandler(h)


def cli() -> object:
    """Get arguments from command line"""
    parser = argparse.ArgumentParser(description="Sudoku solver")
    parser.add_argument(
        "-d", "--display", help="Graphical display", action="store_true"
    )
    parser.add_argument("file", type=argparse.FileType("r"))
    args = parser.parse_args()
    return args


def main():
    args = cli()
    board = reader.read(args.file)
    if board.is_consistent():
        print("Board is good!")
    else:
        print("Board has duplicates; rejected")
        exit(1)
    print(board)
    if args.display:
        display = sudoko_display.Board(board, 800, 800)
    if args.display:
        input("Press enter to shut down")
        display.close()


if __name__ == "__main__":
    main()
