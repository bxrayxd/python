"""
A test module to validate the GeoCollection module functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

from point import Point, MultiPoint
from line import LineString, MultiLineString
from polygon import Polygon, MultiPolygon
from g_collection import GeometryCollection


class TestGeometryCollection(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 1)
        self.p2 = Point(3, 3)
        self.p3 = Point(1, 6)
        self.line = LineString(self.p1, self.p2)
        self.ml = MultiLineString([MultiPoint([self.p1, self.p2, self.p3])])
        self.geo_collection = GeometryCollection([self.p1, self.p2, self.p3, self.line, self.ml])

    def test_initialization(self):
        """Validate that all objects initialize as expected.
        """
        self.assertEqual([self.p1, self.p2, self.p3, self.line, self.ml], self.geo_collection.collection)

    def test_get_coordinate(self):
        """Validate the structure of the coordinates function.
        """
        self.assertRaises(NotImplementedError, lambda: self.geo_collection.get_coordinate())

    def test_get_coordinate_return_type(self):
        """Validate the return type of the coordinates function.
        """
        self.assertRaises(NotImplementedError, lambda: self.geo_collection.get_coordinate())

    def test_is_linear_ring(self):
        self.assertRaises(NotImplementedError, lambda: self.geo_collection.is_linear_ring())

    def test_first_point(self):
        self.assertRaises(NotImplementedError, lambda: self.geo_collection.get_first_point())

    def test_last_point(self):
        self.assertRaises(NotImplementedError, lambda: self.geo_collection.get_last_point())

    def test_repr(self):
        """Validate the structure of the repr function
        """
        expected = ("GeometryCollection([Point(1, 1), Point(3, 3), Point(1, 6), "
                    "LineString(Point(1, 1), Point(3, 3)), "
                    "MultiLineString([MultiPoint([Point(1, 1), Point(3, 3), Point(1, 6)])])])")
        self.assertEqual(expected, self.geo_collection.__repr__())

    def test_str(self):
        """
        Validate the structure of the str return.
        """
        expected = ('{"geometries": ['
                    '{"coordinates": [1, 1], "type": "Point"}, '
                    '{"coordinates": [3, 3], "type": "Point"}, '
                    '{"coordinates": [1, 6], "type": "Point"}, '
                    '{"coordinates": [[1, 1], [3, 3]], "type": "LineString"}, '
                    '{"coordinates": [[[1, 1], [3, 3], [1, 6]]], "type": "MultiLineString"}], '
                    '"type": "GeometryCollection"}')
        self.assertEqual(expected, self.geo_collection.__str__())


if __name__ == '__main__':
    unittest.main()
