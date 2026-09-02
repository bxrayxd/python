
"""
Sudoku board display.
Designed for a simple model/view/controller architecture,
in which the board display knows about the sudoku board,
and not vice versa. Communication from the sudoku board
to the board display is by event notifications through
registered listeners.

Displays a rectangular grid of cells, organized in rows and columns
with row 0 at the top and growing down, column 0 at the left and
growing to the right.  A sequence of unique colors for cells can
be chosen from a color wheel, in addition to colors 'black' and 'white'
which do not appear in the color wheel.
"""

import logging

# Sudoku board configuration options
from sudoku_config import NROWS, NCOLS, SIZE, PENCIL, UNKNOWN
from sudoku_config import COLOR_KNOWN, COLOR_UNKNOWN

# Peer classes from model
import board
from board import EventKind

# Graphics package based on Zelle's simple OO graphics
from graphics import grid

logging.basicConfig()
log = logging.getLogger(__name__)


class Board(object):
    """View of board.Board"""

    def __init__(self, model: board.Board, width: int, height: int):
        """Create a view of the board.
        Width and height are dimensions in pixels.
        """
        self.model = model
        self.grid = grid.Grid(width, height, NROWS, NCOLS, title="Sudoku")

        self.tiles = []
        for row in model.tiles:
            for tile in row:
                self.tiles.append(Tile(self.grid, tile))

    def close(self):
        self.grid.close()


class Tile(board.TileListener):
    """View of a single tile"""

    def __init__(self, grid: grid.Grid, model: board.Tile, scan=True):
        self.grid = grid
        self.model = model
        self.row = model.row
        self.col = model.col
        self.scan = scan
        self.grid.sub_grid_dim(SIZE, SIZE)
        self.grid.draw_boarder_lines()
        self._update(board.TileEvent(self.model, EventKind.TileChanged))
        self.model.add_listener(self)

    def _update(self, event: board.TileEvent):
        """
        Color code the tiles to indicate groups and status

        :param event: The event type.
        """
        if event.kind == EventKind.TileChanged:
            self._color_by_status()
            self._label()
            self.grid.draw_boarder_lines()
        else:
            raise ValueError("Unanticipated event type")

    def _color_by_status(self):
        """
        Color the cell by status.
        """
        if self.model.value == UNKNOWN:
            self.grid.fill_cell(self.row, self.col, COLOR_UNKNOWN)
        else:
            self.grid.fill_cell(self.row, self.col, COLOR_KNOWN)

    def _label(self):
        """
        Add the value to the cell. If unknown, list possible options.
        :return:
        """
        if self.model.value == UNKNOWN:
            self._pencil_marks()
        else:
            self.grid.label_cell(self.row, self.col, self.model.value)

    def _pencil_marks(self):
        """So-called 'pencil marks' are small digits indicating a possible
        choice for a tile value.  We mark the possible choices in a
        grid, leaving a blank for others.
        """
        for i in range(SIZE):
            for j in range(SIZE):
                if self.model.could_be(PENCIL[i][j]):
                    self.grid.sub_label_cell(self.row, self.col, i, j, PENCIL[i][j])

    def notify(self, event: board.TileEvent):
        self._update(event)
