"""Test cases for board.py"""

import time
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
        self.assertEqual('.', self.unknown_tile.value)

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

    def test_remove_all_candidate(self):
        """Remove all from candidates"""
        self.assertTrue(self.unknown_tile.remove_candidates({1, 2, 3, 4, 5, 6, 7, 8, 9}))
        self.assertEqual(set(), self.unknown_tile.candidates)

    def test_remove_nothing_from_candidate(self):
        """Remove nothing. I.e., no used values."""
        deep_copy = set(self.unknown_tile.candidates)
        self.assertFalse(self.unknown_tile.remove_candidates(set()))
        self.assertEqual(deep_copy, self.unknown_tile.candidates)

    def test_remove_one_element_from_candidate(self):
        """Remove only one element from candidates"""
        self.assertTrue(self.unknown_tile.remove_candidates({1}))
        self.assertEqual({2, 3, 4, 5, 6, 7, 8, 9}, self.unknown_tile.candidates)


class TestBoard(unittest.TestCase):

    def test_initial_board(self):
        """init empty board"""
        board = Board()
        sample_tile = board.tiles[0][0]
        self.assertEqual('.', sample_tile.value)
        sample_tile = board.tiles[3][3]
        self.assertEqual('.', sample_tile.value)
        sample_tile = board.tiles[8][8]
        self.assertEqual('.', sample_tile.value)

    def test_load_board(self):
        board = Board()
        board.set_tiles(["123456789", "2345678991", "345678912",
                         "456789123", "567891234", "678912345",
                         "789123456", "891234567", "912345678"])
        sample_tile = board.tiles[0][0]
        self.assertEqual(1, sample_tile.value)
        sample_tile = board.tiles[3][5]
        self.assertEqual(9, sample_tile.value)
        sample_tile = board.tiles[8][8]
        self.assertEqual(8, sample_tile.value)

    def test_read_new_board(self):
        board = sudoku_reader.read("data/00-sample.sdk")
        as_printed = str(board)
        self.assertEqual("32...14..\n"
                         "9..4.2..3\n"
                         "..6.7...9\n"
                         "8.1..5...\n"
                         "...1.6...\n"
                         "...7..1.8\n"
                         "1...9.5..\n"
                         "2..8.4..7\n"
                         "..45...31", as_printed)

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
        """Each group should contain a distinct set of tiles.
        """
        board = Board()
        groups_by_hash = {}
        for group in board.groups:
            hash_sum = 0
            for tile in group:
                hash_sum += hash(tile)
            self.assertNotIn(hash_sum, groups_by_hash,
                             msg=f"Oh no, group {group} is a duplicate!")
            groups_by_hash[hash_sum] = group

    def test_choose_min_tile(self):
        board = Board()
        # We want a predictable, single "best" tile to be chosen,
        # so we'll create a board in which all the 'unknown' tiles
        # have many candidates but exactly one tile has exactly
        # two candidates. It will be easiest to see this if we
        # lay out the board as a matrix.
        board.set_tiles(["....5....",
                         "....4....",
                         ".........",
                         ".........",
                         "123....89",
                         ".........",
                         ".........",
                         ".........",
                         "........."])
        # Tile (4,4) should have just 6,7 as candidates.
        # First we have to remove others with naked_single
        board.obvious_single()
        # Then we can make the choice.
        tile = board.min_choice_tile()
        self.assertEqual(tile.value, ".")
        self.assertEqual(tile.row, 4)
        self.assertEqual(tile.col, 4)
        self.assertEqual(tile.candidates, {6, 7})

    def test_save_restore(self):
        """as_list and set_tiles should work as saving and
        restoring board state.
        """
        board = Board()
        tiles_list = ["......12.", "24..1....", "9.1..4...",
                      "4....365.", "....9....", ".364....1",
                      "...1..5.6", "....5..43", ".72......"]
        board.set_tiles(tiles_list)
        saved = board.as_list()
        self.assertEqual(tiles_list, saved)

    def test_is_complete(self):
        board = Board()
        tiles_list = ["687539124",
                      "243718965",
                      "951264387",
                      "419873652",
                      "725691438",
                      "836425791",
                      "394182576",
                      "168957243",
                      "572346819"]
        board.set_tiles(tiles_list)
        self.assertTrue(board.is_complete())

    def test_is_not_complete(self):
        board = Board()
        tiles_list = [
            "687539124",
            "243718965",
            "951264387",
            "419873652",
            "725691.38",
            "836425791",
            "394182576",
            "168957243",
            "572346819"]
        board.set_tiles(tiles_list)
        self.assertFalse(board.is_complete())


class TestConsistent(unittest.TestCase):
    """Tests of the 'is_consistent' method"""

    def test_good_complete_board(self):
        """Solved board
        This one is from Wikipedia
        """
        board = Board()
        board.set_tiles(["534678912", "672195348", "198342567",
                        "859761423", "426853791", "713924856",
                         "961537284", "287419635", "345286179"])
        self.assertTrue(board.is_consistent())

    def test_good_incomplete(self):
        """unsolved valid board"""
        board = Board()
        board.set_tiles(["...26.7.1", "68..7..9.", "19...45..",
                         "82.1...4.", "..46.29..", ".5...3.28",
                         "..93...74", ".4..5..36", "7.3.18..."])
        self.assertTrue(board.is_consistent())

    def test_bad_column(self):
        """Same value in column"""
        board = Board()
        board.set_tiles(["1........", ".........", ".........",
                         ".........", ".........", ".........",
                         "1........", ".........", "........."])
        self.assertFalse(board.is_consistent())

    def test_bad_row(self):
        """Same value in row"""
        board = Board()
        board.set_tiles([".........", ".........", ".........",
                         ".........", ".2.....2.", ".........",
                         ".........", ".........", "........."])
        self.assertFalse(board.is_consistent())

    def test_bad_block(self):
        """same value in block"""
        board = Board()
        board.set_tiles([".........", "......1..", "........1",
                         ".........", ".........", ".........",
                         ".........", ".........", "........."])
        self.assertFalse(board.is_consistent())


class TestObviousSingle(unittest.TestCase):
    """Simple test of Obvious Single using row, column, and block
    constraints.
    """
    def test_simple_example(self):
        board = Board()
        board.set_tiles([".........",
                         "......1..",
                         "......7..",
                         "......29.",
                         "........4",
                         ".83......",
                         "......5..",
                         ".........",
                         "........."])
        progress = board.obvious_single()
        self.assertTrue(progress, "Should resolve one tile")
        progress = board.obvious_single()
        self.assertTrue(progress, "A few candidates should be eliminated from other tiles")
        progress = board.obvious_single()
        self.assertFalse(progress, "No more progress on this simple example")
        self.assertEqual(str(board), ".........\n"
                                     "......1..\n"
                                     "......7..\n"
                                     "......29.\n"
                                     "........4\n"
                                     ".83...6..\n"
                                     "......5..\n"
                                     ".........\n"
                                     ".........")

    def test_obvious_single_one(self):
        """This puzzle can be solved with multiple rounds of obvious single."""
        board = Board()
        board.set_tiles(["...26.7.1", "68..7..9.", "19...45..",
                         "82.1...4.", "..46.29..", ".5...3.28",
                         "..93...74", ".4..5..36", "7.3.18..."])
        board.solve_using_obvious_singles()
        self.assertEqual(str(board),
                         "\n".join(["435269781", "682571493", "197834562",
                                    "826195347", "374682915", "951743628",
                                    "519326874", "248957136", "763418259"]))


class TestHiddenSingle(unittest.TestCase):
    """Test the Hidden Single tactic, which must be combined with the
    naked single tactic.
    """

    def test_hidden_single_example(self):
        """Simple example from Sadman Sudoku. Since 2 is blocked
        in two columns of the board, it must go into the middle
        column.
        """
        board = Board()
        board.set_tiles([".........", "...2.....",  ".........",
                         "....6....", ".........",  "....8....",
                         ".........", ".........", ".....2..."])
        board.obvious_single()
        board.hidden_single()
        self.assertEqual(str(board),
                         "\n".join(
                        [".........", "...2.....",  ".........",
                         "....6....", "....2....",  "....8....",
                         ".........", ".........", ".....2..."]))

    def test_hidden_single_solve(self):
        """This puzzle can be solved with obvious single
        and hidden single together.
        """
        board = Board()
        board.set_tiles(["......12.", "24..1....", "9.1..4...",
                         "4....365.", "....9....", ".364....1",
                         "...1..5.6", "....5..43", ".72......"])
        board.solve_using_obvious_and_hidden_singles()
        self.assertEqual(str(board),
                         "\n".join(["687539124", "243718965", "951264387",
                                    "419873652", "725691438", "836425791",
                                    "394182576", "168957243", "572346819"]))


class TestGuessAndCheck(unittest.TestCase):

    def test_guess_and_check(self):
        """This can only be solved using all the implemented solutions"""
        board = Board()
        board.set_tiles(["....5..1.", "2........", "5.19..48.",
                         "6...1.24.", "8.......7", ".23.4...1",
                         ".69..28.3", "........4", ".4..8...."])
        board.solve_using_guess_and_check()
        solution = ["497856312", "286134795", "531927486",
                    "675319248", "814265937", "923748561",
                    "169472853", "758693124", "342581679"]
        self.assertEqual(board.as_list(), solution)

    def test_guess_and_check_timing(self):
        """We need to solve the most difficult puzzles in less than 3 sec
        regardless of the machine specs we are using"""
        board = Board()
        board.set_tiles(["....5..1.", "2........", "5.19..48.",
                         "6...1.24.", "8.......7", ".23.4...1",
                         ".69..28.3", "........4", ".4..8...."])
        time_before = time.perf_counter()
        board.solve_using_guess_and_check()
        time_after = time.perf_counter()
        elapsed_seconds = time_after - time_before
        solution = ["497856312", "286134795", "531927486",
                    "675319248", "814265937", "923748561",
                    "169472853", "758693124", "342581679"]
        self.assertEqual(board.as_list(), solution)
        self.assertLess(elapsed_seconds, 3, f"Are you sure your algorithm is fast enough ({elapsed_seconds} >= 3)?")


if __name__ == "__main__":
    unittest.main()
