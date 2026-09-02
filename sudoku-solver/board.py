
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
        pass

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

    def __init__(self, tile: 'Tile', kind: EventKind):
        self.tile = tile
        self.kind = kind

    def __str__(self):
        """Printed representation includes name of concrete subclass"""
        return f"{repr(self.tile)}"


class TileListener(Listener):

    def notify(self, event: TileEvent):
        raise NotImplementedError("TileListener subclass needs to override notify(TileEvent)")


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
        self.value = None
        self.candidates = None
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

    def remove_candidates(self, used_values: Set[int]) -> bool:
        """The used values cannot be a value of this unknown tile.
        We remove those possibilities from the list of candidates.
        If there is exactly one candidate left, we set the
        value of the tile.
        :param used_values: The set of values used in row,
            columns, or block where this tile falls.
        :return: True if we eliminated at least one candidate,
            False if nothing changed (none of the 'used_values'
            was in our candidates set).
        """
        # TODO: remove candidates and update value as given in the description.
        #  Please note that once you remove a candidate or update the value you should
        #  use `self.notify_all(TileEvent(self, EventKind.TileChanged))` if you want
        #  the GUI to be updated!
        pass


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
        # TODO: Add this from project-6

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
        In Sadman Sudoku format
        :return: A string of the Board.
        """
        return "\n".join(self.as_list())

    def as_list(self) -> List[str]:
        """Convert (store) Tile values in a format
        compatible with set_tiles.
        """
        row_syms = []
        for row in self.tiles:
            values = [str(tile.value) for tile in row]
            row_syms.append("".join(values))
        return row_syms

    def is_consistent(self) -> bool:
        """
        Check if the board as a whole is consistent
        according to sudoku rules.
        :return: True if the board is consistent and False otherwise.
        """
        # TODO: Add this from project-7
        pass

    def is_complete(self) -> bool:
        """Check if the board has no tiles with value == UNKNOWN.
        This is different from is_consistent as we don't check
        for validity.
        :return: True if all tiles have value other than UNKNOWN, False
            otherwise.
        """
        # TODO: Go over all tile making sure that none of them have the value UNKNOWN. If any tile has UNKNOWN then
        #  you should return False.
        pass

    def min_choice_tile(self) -> Tile:
        """Returns a tile with value UNKNOWN and minimum number of candidates.

        Precondition: There is at least one tile with value UNKNOWN.

        :return: The tile with the least number of candidates.
        """
        # TODO: Loop through all tiles looking for the tile that has the value UNKONWN and have the least number
        #  of candidates. Return that tile!
        pass

    def obvious_single(self) -> bool:
        """Eliminate candidates and check for sole remaining possibilities.
        We check all rows, columns and blocks for candidates values that we can remove.
        If we find a value that we can remove then we remove it by calling tile.remove_candidates()
        and we return True. Otherwise, we return False.
        Recall the tile.remove_candidates() will assign the tile a value, if it has only one
        remaining value in candidates.

        :return: True if we crossed off at least one candidate. False if we made no progress.
        """
        # TODO: You have to go over each row, column, and block to loop through each tile collecting the
        #  values that are used already. Then again for each tile you should make sure that the used values
        #  are removed from the tile's candidates set (use the Tile.remove_candidates you just implemented).
        #  If you removed any candidate in any tile then you should return True. Otherwise, the tactic
        #  didn't make any change; thus, return False which will indicate the tactic is stuck.
        pass

    def hidden_single(self) -> bool:
        """Check for a hidden candidate.

        Suppose that after applying the hidden single tactic to eliminate some candidates,
        all the unknown tiles still have at least two candidate values.
        But suppose only one of those tiles has candidate value 3. Even though the tile
        that has candidate value 3 may have other candidate values, we know it must
        hold the 3 because there is no other place to put it.

        :return: True changed the value of at least one tile, False if we made no change at all.
        """
        # TODO: Look for hidden singles in the board. That is you will loop through each group
        #  (row, column, and block) to check what values are left. To make this easier I'm providing
        #  a high-level pseudocode.

        """
        For each group:
            keep a deep copy set of the choice we have in general (leftover = set(CHOICES)).
            for each tile in the group:
                if the value of the tile is in the leftover variable, then remove it from it. I recommend using leftovers.discard(tile.value)
            for values in the leftover variable:
                for each tile in the group:
                    count how many times the value appear in each tile's candidates
                If the count is 1 then the value have only one place to go. Place that value to the appropriate tile.
                    In this case and only in this case you return True, Otherwise you return False
        """
        pass

    def solve_using_obvious_singles(self):
        """Repeat solution tactics until we
        don't make any progress, whether
        the board is solved or not.
        """
        progress = True
        while progress:
            progress = self.obvious_single()
        return

    def solve_using_obvious_and_hidden_singles(self):
        """Repeat solution tactics until we
        don't make any progress, whether
        the board is solved or not.
        """
        progress = True
        while progress:
            progress = self.obvious_single()
            self.hidden_single()
        return

    def solve_using_guess_and_check(self) -> bool:
        """General solver; guess-and-check
        combined with obvious_single and hidden_single.
        """
        # TODO: Implement the guess and check for Sudoku as described in the lecture. You need to use the obvious
        #  single and hidden single to make this fast enough. Here is a high-level pseudocode.

        """
        Solve using obvious single and hidden single.
        if the board is complete and consistent return True (base case).
        else:
            save current state (hint: use as_list)
            find the tile with the least number of candidates
            for each value in the tile's candidates:
                make a guess!
                if we solved it (call yourself!)
                    return True
                else:
                    restore the original state (hint use set_tile and the state you just saved above)
            If you reach this point with no luck then you should return False
        """
        pass
