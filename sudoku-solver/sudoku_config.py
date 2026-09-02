"""
This is a configuration file on all what relates to
the Sudoko.
"""
SIZE = 3
NROWS = SIZE * SIZE
NCOLS = SIZE * SIZE
NBLOCKS = SIZE * SIZE

CHOICES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
PENCIL = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
UNKNOWN = '.'

COLOR_BACKGROUND = "#ffffff"  # White
COLOR_KNOWN = "#1e81b0"       # Blue
COLOR_UNKNOWN = "#eeeee4"     # Beige
COLOR_WORKING = "#e28743"     # Orange-ish
