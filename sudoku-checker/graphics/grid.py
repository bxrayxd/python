"""
Grid display.

Displays a rectangular grid of cells, organized in rows and columns
with row 0 at the top and growing down, column 0 at the left and
growing to the right.

Uses the simple graphics module provided by Zelle, which in turn
is built on the Tk graphics package (and which should therefore be
available on all major Python platforms, including Linux, Mac, and
all flavors of Windows at least back to XP). Requires Python 3.6
or greater due to use of type annotations and module 'typing'.
"""

from graphics.graphics import *

BLACK = color_rgb(0, 0, 0)
WHITE = color_rgb(255, 255, 255)
GREY = color_rgb(200, 200, 200)


class Grid(object):
    """Generic grid of rectangles, for Sudoku, Naughts and Crosses, etc.
    Rows and columns are numbered from 0 to n-1, and
    rows are numbered from the top down.
    """

    def __init__(self, width: int, height: int,
                 nrows: int, ncols: int, title: str = "Untitled",
                 background=color_rgb(255, 255, 255)):
        """
        Width and height are dimensions in pixels.

        :param width:
        :param height:
        :param nrows:
        :param ncols:
        :param title:
        :param background:
        """
        self.width = width
        self.height = height
        self.nrows = nrows
        self.ncols = ncols
        self.win = GraphWin(title, width, height)  # create a window
        bkgrnd = Rectangle(Point(0, 0), Point(width, height))  # draw background object in window
        bkgrnd.setFill(background)

        # evenly distribute the space over columns and rows
        self.cell_width = width / ncols
        self.cell_height = height / nrows

    def fill_cell(self, row: int, col: int, color):
        """Fill cell[row, col] with color.

        :param row:  which row the selected cell is in.  Row 0 is the top row,
           row 1 is the next row down, etc.  Row should be between 0
           and one less than the number of rows in the grid.
        :param col:  which column the selected cell is in.  Column 0 is
           the leftmost row, column 1 is the next row to the right, etc.
           Col should be between 0 and one less than the number of columns
           in the grid.
        :param color: What color to fill the select cell with.
        """
        left = col * self.cell_width
        right = (col + 1) * self.cell_width
        top = row * self.cell_height
        bottom = (row + 1) * self.cell_height
        mark = Rectangle(Point(left, bottom), Point(right, top))
        mark.setFill(color)
        mark.draw(self.win)

    def label_cell(self, row, col, text, color=BLACK):
        """Place text label on cell[row, col].

        :param row:  which row the selected cell is in.  Row 0 is the top row,
            row 1 is the next row down, etc.  Row should be between 0
            and one less than the number of rows in the grid.
        :param col:  which column the selected cell is in.  Column 0 is
           the leftmost row, column 1 is the next row to the right, etc.
           Col should be between 0 and one less than the number of columns
           in the grid.
        :param text: string (usually one character) to label the cell with
        :param color: Color of text label
        """
        xcenter = (col + 0.5) * self.cell_width
        ycenter = (row + 0.5) * self.cell_height
        label = Text(Point(xcenter, ycenter), text)
        label.setFace("helvetica")
        label.setSize(20)  # Is there a better way to choose text size?
        label.setFill(color)
        label.draw(self.win)

    def draw_boarder_lines(self):
        v_spacing = self.width / self.n_sub_cols
        h_spacing = self.height / self.n_sub_rows

        for i in range(1, self.n_sub_rows):
            hline = Line(Point(0, h_spacing * i), Point(self.width, h_spacing * i))
            hline.setWidth(5)
            hline.draw(self.win)
        for i in range(1, self.n_sub_cols):
            vline = Line(Point(v_spacing * i, 0), Point(v_spacing * i, self.height))
            vline.setWidth(5)
            vline.draw(self.win)

    def sub_grid_dim(self, rows, cols):
        """Divide each cell into rows x cols for sub-labeling
        (like "pencil marks" in Sudoku).

        Effects: Affects behavior of sub_label_cell.

        :param rows: The number of rows of sub-cell in a cell.
        :param cols:  The number of columns of sub-cell in a cell.
        """
        self.n_sub_rows = rows
        self.n_sub_cols = cols

    def sub_label_cell(self, row, col, sub_row, sub_col, text, color=BLACK):
        """Place label in subrow, subcol of row, col.

        :param row: Row of major grid (counting 0 as top row)
        :param col: Column of major grid (counting 0 as leftmost column)
        :param sub_row: Row in minor (interior) grid of cell
        :param sub_col: Column in minor (interior) grid of cell
        :param text: Label (usually one character) to place there
        color: color of text
        """
        xcenter = self.cell_width * (col + (sub_col + 0.5) / self.n_sub_cols)
        ycenter = self.cell_height * (row + (sub_row + 0.5) / self.n_sub_rows)
        label = Text(Point(xcenter, ycenter), text)
        label.setFace("helvetica")
        label.setSize(10)
        label.setFill(color)
        label.draw(self.win)

    def close(self):
        """ Close the graphics window (shut down graphics). """
        self.win.close()


def main():
    """Smoke test"""
    grid = Grid(500, 500, 9, 9)
    grid.sub_grid_dim(3, 3)
    for row in range(9):
        for col in range(9):
            grid.fill_cell(row, col, color_rgb(200, 200, 200))
            grid.label_cell(row, col, f"{row + 1},{col + 1}")
    grid.draw_boarder_lines()

    input('Press enter to close')


if __name__ == "__main__":
    main()
