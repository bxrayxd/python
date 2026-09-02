"""
Reading and writing Sudoku boards. We use the minimal
subset of the SadMan Sudoku ".sdk" format.
"""

import board as sudoku_board
from sudoku_config import NROWS
from typing import Union
from io import IOBase

import logging
log = logging.getLogger(__name__)


def read(f: Union[IOBase, str], board: sudoku_board.Board = None) -> sudoku_board.Board:
    """Read a Sudoku board from a file.  Pass in a path
    or an already opened file. Optionally pass in a board to be
    filled.
    """
    if isinstance(f, str):
        log.debug("Reading from string")
        f = open(f, "r")
    else:
        log.debug(f"Reading from file {f}")
    if board is None:
        board = sudoku_board.Board()
    values = []
    for row in f:
        row = row.strip()
        log.debug(f"Reading row |{row}|")
        values.append(row)
        if len(row) != NROWS:
            raise IOError(f"Puzzle row wrong length: {row}")
    log.debug(f"Read values: {values}")
    if len(values) != NROWS:
        raise IOError(f"Wrong number of rows in {values}")
    board.set_tiles(values)
    f.close()
    return board
