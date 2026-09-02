"""
A Sudoku board holds a matrix of tiles.
Each row and column and also sub-blocks
are treated as a group, each group must contain
exactly one occurrence of each of the symbol choices.
"""

import enum
from typing import Sequence, List, Set

from sudoku_config import CHOICES, UNKNOWN, SIZE
from sudoku_config import NROWS, NCOLS


class Event(object):
    """Abstract base class of all events, both for MVC
    and for other purposes.
    """

    pass


class Listener(object):
    """
    Listeners (base class)

    Abstract base class for listeners.
    Subclass this to make the notification do
    something useful.
    """

    def __init__(self):
        """Default constructor for simple listeners without state"""

    def notify(self, event: Event):
        """The 'notify' method of the base class must be
        overridden in concrete classes.
        """
        raise NotImplementedError("You must override Listener.notify")


class EventKind(enum.Enum):
    """
    Events and listeners for Tile objects
    """

    TileChanged = 1
    TileGuessed = 2


class TileEvent(Event):
    """Abstract base class for things that happen
    to tile(s). We always indicate the tile. Concrete
    subclasses indicate the nature of the event.
    """

    def __init__(self, tile: "Tile", kind: EventKind):
        self.tile = tile
        self.kind = kind

    def __str__(self):
        """Printed representation includes name of concrete subclass"""
        return f"{repr(self.tile)}"


class TileListener(Listener):
    def notify(self, event: TileEvent):
        raise NotImplementedError(
            "TileListener subclass needs to override notify(TileEvent)"
        )


class Listenable:
    """Objects to which listeners (like a view component) can be attached"""

    def __init__(self):
        self.listeners = []

    def add_listener(self, listener: Listener):
        self.listeners.append(listener)

    def notify_all(self, event: Event):
        for listener in self.listeners:
            listener.notify(event)


class Tile(Listenable):
    """One tile on the Sudoku grid.
    Public attributes (read-only): value, which will be either
    UNKNOWN or an element of CHOICES; candidates, which will
    be a set drawn from CHOICES.  If value is an element of
    CHOICES,then candidates will be the singleton containing
    value.  If candidates is empty, then no tile value can
    be consistent with other tile values in the grid.
    value is a public read-only attribute; change it
    only through the access method set_value or indirectly
    through method remove_candidates.
    """

    def __init__(self, row: int, col: int, value=UNKNOWN):
        super().__init__()
        assert value == UNKNOWN or value in CHOICES
        self.row = row
        self.col = col
        self.set_value(value)

    def set_value(self, value: str):
        """
        Set the value of the tile.
        :param value: The value either a number of unknown.
        """
        if value == UNKNOWN:
            self.value = UNKNOWN
            self.candidates = set(CHOICES)
        else:
            self.value = int(value)
            self.candidates = {int(value)}
        self.notify_all(TileEvent(self, EventKind.TileChanged))

    def __str__(self):
        """
        Print Tile!
        :return: A string representation of the object
        """
        return f"{self.value}"

    def __repr__(self):
        """
        Repr the Tile!
        :return: A string representation of Tile.
        """
        return f"Tile({self.row}, {self.col}, '{self.value}')"

    def __hash__(self) -> int:
        """Hash on position only (not value)
        to identify the tile with certainty.
        """
        return hash((self.row, self.col))

    def could_be(self, value: str) -> bool:
        """True iff value is a candidate value for this tile"""
        return value in self.candidates


class Board(object):
    """Board class
    A board has a matrix of tiles
    """

    def __init__(self):
        """The empty board"""
        # Row/Column structure: Each row contains columns
        self.tiles: List[List[Tile]] = []
        for row in range(NROWS):
            cols = []
            for col in range(NCOLS):
                cols.append(Tile(row, col))
            self.tiles.append(cols)

        # create an alias for each group for easy access.
        self.groups: List[List[Tile]] = []

        # adding rows to groups
        for row in self.tiles:
            self.groups.append(row)

        # adding columns to groups
        for col_num in range(NCOLS):
            col = []
            for row_num in range(NROWS):
                col.append(self.tiles[row_num][col_num])
            self.groups.append(col)

        # adding blocks to groups
        for block_row in range(SIZE):
            for block_col in range(SIZE):
                group = []
                for row in range(SIZE):
                    for col in range(SIZE):
                        row_addr = (SIZE * block_row) + row
                        col_addr = (SIZE * block_col) + col
                        group.append(self.tiles[row_addr][col_addr])
                self.groups.append(group)

    def set_tiles(self, tile_values: Sequence[Sequence[str]]):
        """Set the tile values a list of lists or a list of strings"""
        for row_num in range(NROWS):
            for col_num in range(NCOLS):
                tile = self.tiles[row_num][col_num]
                tile.set_value(tile_values[row_num][col_num])

    def __str__(self) -> str:
        """
        In Sadman Sudoku format. This is the same format found in the file
        named data/00-sample.sdk
        :return: A string of the Board.
        """
        result = ""
        for row in self.tiles:
            for tile in row:
                if tile.value == UNKNOWN:
                    result += "."
                else:
                    result += str(tile.value)
            result += "\n"
        return result.strip()

    def is_consistent(self) -> bool:
        """
        Check if the board as a whole is consistent
        according to sudoku rules.
        :return: True if the board is consistent and False otherwise.
        """

        """
        for each row, column and block
            init a set named 'used_symbols' to hold the used symbol in each row, column or block. Note that a set is
            initialized by 'set()'
            for each tile in the group (row, column or block)
                if the tile value is in CHOICES
                    check if the tile value is in 'used_symbols'
                        if so we fail (return False)
                    otherwise add the tile value to the set of 'used_symbols'
        if we reach this point without failure, then rerun True (the board is consistent) 
        """
        for group in self.groups:
            used_symbols = set()
            for tile in group:
                if tile.value in CHOICES:
                    if tile.value in used_symbols:
                        return False
                    else:
                        used_symbols.add(tile.value)
        return True
