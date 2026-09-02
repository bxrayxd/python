"""
A test module to validate the point module functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

from point import Point, MultiPoint


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(5.2, 3.4)
        self.p2 = Point(-1.4, 2.5)

    def test_initialization(self):
        """Validate that all objects initialize as expected.
        """

        self.assertEqual(self.p1.x, 5.2)
        self.assertEqual(self.p1.y, 3.4)

        self.assertEqual(self.p2.x, -1.4)
        self.assertEqual(self.p2.y, 2.5)

    def test_get_coordinate(self):
        """Validate the structure of the coordinates function.
        """
        self.assertEqual(self.p1.get_coordinate(), "[5.2, 3.4]")
        self.assertEqual(self.p2.get_coordinate(), "[-1.4, 2.5]")

    def test_get_coordinate_return_type(self):
        """Validate the return type of the coordinates function.
        """

        self.assertIsInstance(self.p1.get_coordinate(), str)
        self.assertIsInstance(self.p2.get_coordinate(), str)

    def test_is_linear_ring(self):
        self.assertRaises(NotImplementedError, lambda: self.p1.is_linear_ring())
        self.assertRaises(NotImplementedError, lambda: self.p2.is_linear_ring())

    def test_get_first_point(self):
        self.assertRaises(NotImplementedError, lambda: self.p1.get_first_point())
        self.assertRaises(NotImplementedError, lambda: self.p2.get_first_point())

    def test_get_last_point(self):
        self.assertRaises(NotImplementedError, lambda: self.p1.get_last_point())
        self.assertRaises(NotImplementedError, lambda: self.p2.get_last_point())

    def test_repr(self):
        """Validate the structure of the repr function
        """
        self.assertEqual(self.p1.__repr__(), "Point(5.2, 3.4)")
        self.assertEqual(self.p2.__repr__(), "Point(-1.4, 2.5)")

    def test_str(self):
        """
        Validate the structure of the str return.
        """
        self.assertEqual(self.p1.__str__(), '{"coordinates": [5.2, 3.4], "type": "Point"}')
        self.assertEqual(self.p2.__str__(), '{"coordinates": [-1.4, 2.5], "type": "Point"}')

    def test_eq(self):
        self.assertEqual(Point(1, 1), Point(1, 1))

    def test_not_eq(self):
        self.assertNotEqual(self.p1, self.p2)


class TestMultiPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(5.2, 3.4)
        self.p2 = Point(-1.4, 2.5)
        self.mp1 = MultiPoint([self.p1, self.p2])
        self.mp2 = MultiPoint([self.p2, self.p1])

    def test_initialization(self):
        """Validate that all objects initialize as expected.
        """
        self.assertEqual(self.mp1.points, [self.p1, self.p2])
        self.assertEqual(self.mp2.points, [self.p2, self.p1])

    def test_get_coordinate(self):
        """Validate the structure of the coordinates function.
        """
        self.assertEqual(self.mp1.get_coordinate(), "[[5.2, 3.4], [-1.4, 2.5]]")
        self.assertEqual(self.mp2.get_coordinate(), "[[-1.4, 2.5], [5.2, 3.4]]")

    def test_get_coordinate_return_type(self):
        """Validate the return type of the coordinates function.
        """

        self.assertIsInstance(self.mp1.get_coordinate(), str)
        self.assertIsInstance(self.mp2.get_coordinate(), str)

    def test_repr(self):
        """Validate the structure of the repr function
        """
        self.assertEqual(self.mp1.__repr__(), "MultiPoint([Point(5.2, 3.4), Point(-1.4, 2.5)])")
        self.assertEqual(self.mp2.__repr__(), "MultiPoint([Point(-1.4, 2.5), Point(5.2, 3.4)])")

    def test_str(self):
        """
        Validate the structure of the str return.
        """
        self.assertEqual(self.mp1.__str__(), '{"coordinates": [[5.2, 3.4], [-1.4, 2.5]], "type": "MultiPoint"}')
        self.assertEqual(self.mp2.__str__(), '{"coordinates": [[-1.4, 2.5], [5.2, 3.4]], "type": "MultiPoint"}')

    def test_linear_ring(self):
        mp = MultiPoint([Point(1, 1), Point(2, 1), Point(2, 2), Point(1, 2), Point(1, 1)])
        self.assertTrue(mp.is_linear_ring())

    def test_not_linear_ring(self):
        mp = MultiPoint([Point(1, 1), Point(2, 1), Point(2, 2), Point(1, 2), Point(10, 10)])
        self.assertFalse(mp.is_linear_ring())

    def test_not_linear_ring_on_empty(self):
        mp = MultiPoint([])
        self.assertFalse(mp.is_linear_ring())

    def test_get_first_point(self):
        self.assertEqual(self.p1, self.mp1.get_first_point())
        self.assertEqual(self.p2, self.mp2.get_first_point())

    def test_get_last_point(self):
        self.assertEqual(self.p2, self.mp1.get_last_point())
        self.assertEqual(self.p1, self.mp2.get_last_point())

    def test_no_first_point(self):
        mp = MultiPoint([])
        self.assertRaises(KeyError, lambda: mp.get_first_point())

    def test_no_last_point(self):
        mp = MultiPoint([])
        self.assertRaises(KeyError, lambda: mp.get_last_point())


if __name__ == '__main__':
    unittest.main()
