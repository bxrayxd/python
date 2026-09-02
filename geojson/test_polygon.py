"""
A test module to validate the polygon module functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

from point import Point, MultiPoint
from line import LineString, MultiLineString
from polygon import Polygon, MultiPolygon


class TestPolygon(unittest.TestCase):

    def setUp(self):
        self.mls1 = MultiLineString([MultiPoint([Point(2.38, 57.322),
                                                 Point(-120.43, 19.15),
                                                 Point(23.194, -20.28),
                                                 Point(2.38, 57.322)])])
        self.pol1 = Polygon(self.mls1)

        # TODO: [For Instructor], Such declaration of the MultiLineString to be used with
        #   with the Polygon, will cause the points in  get_coordinates to be nested.
        #   For example, get_coordinates will be [[[0, 0], [10, 0]], [[10, 10], [0, 10], [0, 0]]]
        #   instead of [[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]]
        #   A redesign of how the get_coordinates works at all classes must take place for
        #   this to work!
        # self.mls2 = MultiLineString([
        #     LineString(Point(0, 0), Point(10, 0)),
        #     MultiPoint([Point(10, 10), Point(0, 10), Point(0, 0)])
        # ])

        self.mls2 = MultiLineString([
            MultiPoint([Point(0, 0), Point(10, 0),
                        Point(10, 10), Point(0, 10),
                        Point(0, 0)])
        ])

        self.pol2 = Polygon(self.mls2)

    def test_initialization(self):
        """Validate that all objects initialize as expected.
        """

        self.assertEqual(self.pol1.polygon, self.mls1)
        self.assertEqual(self.pol2.polygon, self.mls2)

    def test_init_non_linear_ring(self):
        mls = MultiLineString([MultiPoint([Point(2.38, 57.322),
                                           Point(-120.43, 19.15),
                                           Point(23.194, -20.28)])])
        self.assertRaises(ValueError, lambda: Polygon(mls))

    def test_get_coordinate(self):
        """Validate the structure of the coordinates function.
        """
        self.assertEqual("[[[2.38, 57.322], [-120.43, 19.15], [23.194, -20.28], [2.38, 57.322]]]",
                         self.pol1.get_coordinate())
        self.assertEqual("[[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]]",
                         self.pol2.get_coordinate())

    def test_get_coordinate_return_type(self):
        """Validate the return type of the coordinates function.
        """

        self.assertIsInstance(self.pol1.get_coordinate(), str)
        self.assertIsInstance(self.pol2.get_coordinate(), str)

    def test_is_linear_ring(self):
        self.assertTrue(self.pol1.is_linear_ring())
        self.assertTrue(self.pol2.is_linear_ring())

    def test_first_point(self):
        self.assertEqual(Point(2.38, 57.322), self.pol1.get_first_point())
        self.assertEqual(Point(0, 0), self.pol2.get_first_point())

    def test_last_point(self):
        self.assertEqual(Point(2.38, 57.322), self.pol1.get_last_point())
        self.assertEqual(Point(0, 0), self.pol2.get_last_point())

    def test_repr(self):
        """Validate the structure of the repr function
        """
        self.assertEqual("Polygon(MultiLineString([MultiPoint([Point(2.38, 57.322), Point(-120.43, 19.15), "
                         "Point(23.194, -20.28), Point(2.38, 57.322)])]))", self.pol1.__repr__())
        self.assertEqual("Polygon(MultiLineString([MultiPoint([Point(0, 0), Point(10, 0), Point(10, 10), "
                         "Point(0, 10), Point(0, 0)])]))", self.pol2.__repr__())

    def test_str(self):
        """
        Validate the structure of the str return.
        """
        self.assertEqual('{"coordinates": [[[2.38, 57.322], [-120.43, 19.15], [23.194, -20.28], '
                         '[2.38, 57.322]]], "type": "Polygon"}', self.pol1.__str__())
        self.assertEqual('{"coordinates": [[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]], "type": "Polygon"}',
                         self.pol2.__str__())


class TestMultiPolygon(unittest.TestCase):

    def setUp(self):
        self.mls1 = MultiLineString([MultiPoint([Point(0, 0),
                                                 Point(10, 0),
                                                 Point(10, 10),
                                                 Point(0, 10),
                                                 Point(0, 0)])])
        self.mls2 = MultiLineString([MultiPoint([Point(11, 11),
                                                 Point(14, 11),
                                                 Point(14, 14),
                                                 Point(11, 14),
                                                 Point(11, 11)])])
        self.mls3 = MultiLineString([MultiPoint([Point(1, 1),
                                                 Point(4, 1),
                                                 Point(4, 4),
                                                 Point(1, 4),
                                                 Point(1, 1)])])

        self.pol1 = Polygon(self.mls1)
        self.pol2 = Polygon(self.mls2)
        self.pol3 = Polygon(self.mls3)

        self.mpol1 = MultiPolygon([self.pol1, self.pol2])
        self.mpol2 = MultiPolygon([self.pol2, self.pol3])
        self.mpol3 = MultiPolygon([self.pol1, self.pol2, self.pol3])

    def test_initialization(self):
        """Validate that all objects initialize as expected.
        """
        self.assertEqual([self.pol1, self.pol2], self.mpol1.polygons)
        self.assertEqual([self.pol2, self.pol3], self.mpol2.polygons)
        self.assertEqual([self.pol1, self.pol2, self.pol3], self.mpol3.polygons)

    def test_get_coordinate(self):
        """Validate the structure of the coordinates function.
        """

        self.assertEqual("[[[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]], "
                         "[[[11, 11], [14, 11], [14, 14], [11, 14], [11, 11]]]]", self.mpol1.get_coordinate())
        self.assertEqual("[[[[11, 11], [14, 11], [14, 14], [11, 14], [11, 11]]], "
                         "[[[1, 1], [4, 1], [4, 4], [1, 4], [1, 1]]]]", self.mpol2.get_coordinate())
        self.assertEqual("[[[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]], "
                         "[[[11, 11], [14, 11], [14, 14], [11, 14], [11, 11]]], "
                         "[[[1, 1], [4, 1], [4, 4], [1, 4], [1, 1]]]]", self.mpol3.get_coordinate())

    def test_is_linear_ring(self):
        self.assertTrue(self.mpol1.is_linear_ring())
        self.assertTrue(self.mpol2.is_linear_ring())
        self.assertTrue(self.mpol3.is_linear_ring())

    def test_get_first_point(self):
        self.assertRaises(NotImplementedError, lambda: self.mpol1.get_first_point())
        self.assertRaises(NotImplementedError, lambda: self.mpol2.get_first_point())
        self.assertRaises(NotImplementedError, lambda: self.mpol3.get_first_point())

    def test_get_last_point(self):
        self.assertRaises(NotImplementedError, lambda: self.mpol1.get_last_point())
        self.assertRaises(NotImplementedError, lambda: self.mpol2.get_last_point())
        self.assertRaises(NotImplementedError, lambda: self.mpol3.get_last_point())

    def test_get_coordinate_return_type(self):
        """Validate the return type of the coordinates function.
        """
        self.assertIsInstance(self.mpol1.get_coordinate(), str)
        self.assertIsInstance(self.mpol2.get_coordinate(), str)
        self.assertIsInstance(self.mpol3.get_coordinate(), str)

    def test_repr(self):
        """Validate the structure of the repr function
        """
        expected1 = ("MultiPolygon([Polygon(MultiLineString([MultiPoint([Point(0, 0), Point(10, 0), "
                     "Point(10, 10), Point(0, 10), Point(0, 0)])])), "
                     "Polygon(MultiLineString([MultiPoint([Point(11, 11), Point(14, 11), Point(14, 14), "
                     "Point(11, 14), Point(11, 11)])]))])")
        self.assertEqual(expected1, self.mpol1.__repr__())

        expected2 = ("MultiPolygon([Polygon(MultiLineString([MultiPoint([Point(11, 11), Point(14, 11), "
                     "Point(14, 14), Point(11, 14), Point(11, 11)])])), "
                     "Polygon(MultiLineString([MultiPoint([Point(1, 1), Point(4, 1), Point(4, 4), "
                     "Point(1, 4), Point(1, 1)])]))])")
        self.assertEqual(expected2, self.mpol2.__repr__())

        expected3 = ("MultiPolygon([Polygon(MultiLineString([MultiPoint([Point(0, 0), Point(10, 0), Point(10, 10), "
                     "Point(0, 10), Point(0, 0)])])), "
                     "Polygon(MultiLineString([MultiPoint([Point(11, 11), Point(14, 11), Point(14, 14), "
                     "Point(11, 14), Point(11, 11)])])), "
                     "Polygon(MultiLineString([MultiPoint([Point(1, 1), Point(4, 1), Point(4, 4), "
                     "Point(1, 4), Point(1, 1)])]))])")
        self.assertEqual(expected3, self.mpol3.__repr__())

    def test_str(self):
        """
        Validate the structure of the str return.
        """
        expected1 = ('{"coordinates": [[[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]], '
                     '[[[11, 11], [14, 11], [14, 14], [11, 14], [11, 11]]]], "type": "MultiPolygon"}')
        self.assertEqual(expected1, self.mpol1.__str__())

        expected2 = ('{"coordinates": [[[[11, 11], [14, 11], [14, 14], [11, 14], [11, 11]]], '
                     '[[[1, 1], [4, 1], [4, 4], [1, 4], [1, 1]]]], "type": "MultiPolygon"}')
        self.assertEqual(expected2, self.mpol2.__str__())

        expected3 = ('{"coordinates": [[[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]], '
                     '[[[11, 11], [14, 11], [14, 14], [11, 14], [11, 11]]], [[[1, 1], '
                     '[4, 1], [4, 4], [1, 4], [1, 1]]]], "type": "MultiPolygon"}')
        self.assertEqual(expected3, self.mpol3.__str__())


if __name__ == '__main__':
    unittest.main()
