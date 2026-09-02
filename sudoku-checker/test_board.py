"""Test cases for board.py"""

import unittest

import reader as sudoku_reader
from board import *
from sudoku_config import *


class TestTile(unittest.TestCase):
    def setUp(self) -> None:
        self.unknown_tile = Tile(3, 2, UNKNOWN)
        self.known_tile = Tile(5, 7, 9)

    def test_init_unknown_row_and_col(self):
        self.assertEqual(3, self.unknown_tile.row)
        self.assertEqual(2, self.unknown_tile.col)

    def test_init_unknown_value(self):
        self.assertEqual(".", self.unknown_tile.value)

    def test_init_unknown_candidates(self):
        self.assertEqual(set(CHOICES), self.unknown_tile.candidates)

    def test_init_unknown_repr(self):
        self.assertEqual("Tile(3, 2, '.')", repr(self.unknown_tile))

    def test_init_unknown_str(self):
        self.assertEqual(".", str(self.unknown_tile))

    def test_init_known_row_and_col(self):
        self.assertEqual(5, self.known_tile.row)
        self.assertEqual(7, self.known_tile.col)

    def test_init_known_value(self):
        self.assertEqual(9, self.known_tile.value)

    def test_init_known_candidates(self):
        self.assertEqual({9}, self.known_tile.candidates)

    def test_init_known_repr(self):
        self.assertEqual("Tile(5, 7, '9')", repr(self.known_tile))

    def test_init_known_str(self):
        self.assertEqual("9", str(self.known_tile))


class TestBoard(unittest.TestCase):
    def test_initial_board(self):
        """init empty board"""
        board = Board()
        sample_tile = board.tiles[0][0]
        self.assertEqual(".", sample_tile.value)
        sample_tile = board.tiles[3][3]
        self.assertEqual(".", sample_tile.value)
        sample_tile = board.tiles[8][8]
        self.assertEqual(".", sample_tile.value)

    def test_load_board(self):
        board = Board()
        board.set_tiles(
            [
                "123456789",
                "2345678991",
                "345678912",
                "456789123",
                "567891234",
                "678912345",
                "789123456",
                "891234567",
                "912345678",
            ]
        )
        sample_tile = board.tiles[0][0]
        self.assertEqual(1, sample_tile.value)
        sample_tile = board.tiles[3][5]
        self.assertEqual(9, sample_tile.value)
        sample_tile = board.tiles[8][8]
        self.assertEqual(8, sample_tile.value)

    def test_read_new_board(self):
        board = sudoku_reader.read("data/00-sample.sdk")
        as_printed = str(board)
        self.assertEqual(
            "32...14..\n"
            "9..4.2..3\n"
            "..6.7...9\n"
            "8.1..5...\n"
            "...1.6...\n"
            "...7..1.8\n"
            "1...9.5..\n"
            "2..8.4..7\n"
            "..45...31",
            as_printed,
        )

    def test_count_tile_groups(self):
        """Every tile should appear in exactly three groups
        (regardless of board size).
        """
        board = Board()
        counts = {}
        for group in board.groups:
            for tile in group:
                if tile not in counts:
                    counts[tile] = 0
                counts[tile] += 1
        for tile in counts:
            self.assertEqual(counts[tile], 3)

    def test_groups_are_distinct(self):
        """Each group should contain a distinct set of tiles."""
        board = Board()
        groups_by_hash = {}
        for group in board.groups:
            hash_sum = 0
            for tile in group:
                hash_sum += hash(tile)
            self.assertNotIn(
                hash_sum, groups_by_hash, msg=f"Oh no, group {group} is a duplicate!"
            )
            groups_by_hash[hash_sum] = group


class TestConsistent(unittest.TestCase):
    """Tests of the 'is_consistent' method"""

    def test_good_complete_board(self):
        """Solved board
        This one is from Wikipedia
        """
        board = Board()
        board.set_tiles(
            [
                "534678912",
                "672195348",
                "198342567",
                "859761423",
                "426853791",
                "713924856",
                "961537284",
                "287419635",
                "345286179",
            ]
        )
        self.assertTrue(board.is_consistent())

    def test_good_incomplete(self):
        """unsolved valid board"""
        board = Board()
        board.set_tiles(
            [
                "...26.7.1",
                "68..7..9.",
                "19...45..",
                "82.1...4.",
                "..46.29..",
                ".5...3.28",
                "..93...74",
                ".4..5..36",
                "7.3.18...",
            ]
        )
        self.assertTrue(board.is_consistent())

    def test_bad_column(self):
        """Same value in column"""
        board = Board()
        board.set_tiles(
            [
                "1........",
                ".........",
                ".........",
                ".........",
                ".........",
                ".........",
                "1........",
                ".........",
                ".........",
            ]
        )
        self.assertFalse(board.is_consistent())

    def test_bad_row(self):
        """Same value in row"""
        board = Board()
        board.set_tiles(
            [
                ".........",
                ".........",
                ".........",
                ".........",
                ".2.....2.",
                ".........",
                ".........",
                ".........",
                ".........",
            ]
        )
        self.assertFalse(board.is_consistent())

    def test_bad_block(self):
        """same value in block"""
        board = Board()
        board.set_tiles(
            [
                ".........",
                "......1..",
                "........1",
                ".........",
                ".........",
                ".........",
                ".........",
                ".........",
                ".........",
            ]
        )
        self.assertFalse(board.is_consistent())


if __name__ == "__main__":
    unittest.main()
