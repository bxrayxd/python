"""
A test module to validate the line module functionalities.

Author: Ziyad Alsaeed
Email: zalsaeed@qu.edu.sa
"""


import unittest

from point import Point, MultiPoint
from line import LineString, MultiLineString


class TestLineString(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(6.524, 33.1265)
        self.p2 = Point(16.88, -21.24)

        self.ls1 = LineString(self.p1, self.p2)
        self.ls2 = LineString(self.p2, self.p1)

    def test_initialization(self):
        """Validate that all objects initialize as expected.
        """

        self.assertEqual(self.ls1.p1, self.p1)
        self.assertEqual(self.ls1.p2, self.p2)

        self.assertEqual(self.ls2.p1, self.p2)
        self.assertEqual(self.ls2.p2, self.p1)

    def test_get_coordinate(self):
        """Validate the structure of the coordinates function.
        """
        self.assertEqual(self.ls1.get_coordinate(), "[[6.524, 33.1265], [16.88, -21.24]]")
        self.assertEqual(self.ls2.get_coordinate(), "[[16.88, -21.24], [6.524, 33.1265]]")

    def test_get_coordinate_return_type(self):
        """Validate the return type of the coordinates function.
        """

        self.assertIsInstance(self.ls1.get_coordinate(), str)
        self.assertIsInstance(self.ls2.get_coordinate(), str)

    def test_repr(self):
        """Validate the structure of the repr function
        """
        self.assertEqual(self.ls1.__repr__(), "LineString(Point(6.524, 33.1265), Point(16.88, -21.24))")
        self.assertEqual(self.ls2.__repr__(), "LineString(Point(16.88, -21.24), Point(6.524, 33.1265))")

    def test_str(self):
        """
        Validate the structure of the str return.
        """
        self.assertEqual(self.ls1.__str__(), '{"coordinates": [[6.524, 33.1265], [16.88, -21.24]], '
                                             '"type": "LineString"}')
        self.assertEqual(self.ls2.__str__(), '{"coordinates": [[16.88, -21.24], [6.524, 33.1265]], '
                                             '"type": "LineString"}')


class TestMultiLineString(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(6.524, 33.1265)
        self.p2 = Point(16.88, -21.24)

        self.mp1 = MultiPoint([self.p1, self.p2])
        self.mp2 = MultiPoint([self.p2, self.p1])

        self.ls1 = LineString(self.p1, self.p2)
        self.ls2 = LineString(self.p2, self.p1)

        self.mls1 = MultiLineString([self.ls1])
        self.mls2 = MultiLineString([self.ls1, self.ls2])
        self.mls3 = MultiLineString([self.ls2, self.ls1])
        self.mls4 = MultiLineString([self.mp1, self.mp2])
        self.mls5 = MultiLineString([self.mp2, self.mp1])
        self.mls6 = MultiLineString([self.ls1, self.mp1])

    def test_initialization(self):
        """Validate that all objects initialize as expected.
        """
        self.assertEqual(self.mls1.lines, [self.ls1])
        self.assertEqual(self.mls2.lines, [self.ls1, self.ls2])
        self.assertEqual(self.mls3.lines, [self.ls2, self.ls1])
        self.assertEqual(self.mls4.lines, [self.mp1, self.mp2])
        self.assertEqual(self.mls5.lines, [self.mp2, self.mp1])
        self.assertEqual(self.mls6.lines, [self.ls1, self.mp1])

        self.assertEqual(self.mls1.lines[0].p1.x, 6.524)
        self.assertEqual(self.mls1.lines[0].p1.y, 33.1265)

    def test_get_coordinate(self):
        """Validate the structure of the coordinates function.
        """
        self.assertEqual(self.mls1.get_coordinate(), "[[[6.524, 33.1265], [16.88, -21.24]]]")
        self.assertEqual(self.mls2.get_coordinate(),
                         "[[[6.524, 33.1265], [16.88, -21.24]], [[16.88, -21.24], [6.524, 33.1265]]]")
        self.assertEqual(self.mls3.get_coordinate(),
                         "[[[16.88, -21.24], [6.524, 33.1265]], [[6.524, 33.1265], [16.88, -21.24]]]")
        self.assertEqual(self.mls4.get_coordinate(),
                         "[[[6.524, 33.1265], [16.88, -21.24]], [[16.88, -21.24], [6.524, 33.1265]]]")
        self.assertEqual(self.mls5.get_coordinate(),
                         "[[[16.88, -21.24], [6.524, 33.1265]], [[6.524, 33.1265], [16.88, -21.24]]]")
        self.assertEqual(self.mls6.get_coordinate(),
                         "[[[6.524, 33.1265], [16.88, -21.24]], [[6.524, 33.1265], [16.88, -21.24]]]")

    def test_get_coordinate_return_type(self):
        """Validate the return type of the coordinates function.
        """
        self.assertIsInstance(self.mls1.get_coordinate(), str)
        self.assertIsInstance(self.mls2.get_coordinate(), str)

    def test_repr(self):
        """Validate the structure of the repr function
        """
        self.assertEqual(self.mls1.__repr__(),
                         "MultiLineString([LineString(Point(6.524, 33.1265), Point(16.88, -21.24))])")
        self.assertEqual(self.mls2.__repr__(),
                         "MultiLineString([LineString(Point(6.524, 33.1265), Point(16.88, -21.24)), "
                         "LineString(Point(16.88, -21.24), Point(6.524, 33.1265))])")
        self.assertEqual(self.mls3.__repr__(),
                         "MultiLineString([LineString(Point(16.88, -21.24), Point(6.524, 33.1265)), "
                         "LineString(Point(6.524, 33.1265), Point(16.88, -21.24))])")
        self.assertEqual(self.mls4.__repr__(),
                         "MultiLineString([MultiPoint([Point(6.524, 33.1265), Point(16.88, -21.24)]), "
                         "MultiPoint([Point(16.88, -21.24), Point(6.524, 33.1265)])])")

        # mls5 is not tested!

        self.assertEqual(self.mls6.__repr__(),
                         "MultiLineString([LineString(Point(6.524, 33.1265), Point(16.88, -21.24)), "
                         "MultiPoint([Point(6.524, 33.1265), Point(16.88, -21.24)])])")

    def test_repr_left_for_students(self):
        # TODO: Fix this test case. We will not grade your work on fixing this test case. However,
        #   we left it for you so that you get to recognize the details. For help compare this to the
        #   test case written fro self.mls3

        # self.assertEqual(self.mls5.__repr__(),
        #                  "MultiLineString([MultiPoint([Point(16.88, -21.24), Point(6.524, 33.1265)]), "
        #                  "MultiPoint([Point(6.524, 33.1265), Point(16.88, -21.24)])])")
        # self.fail()
        pass

    def test_str(self):
        """
        Validate the structure of the str return.
        """
        self.assertEqual(self.mls1.__str__(),
                         '{"coordinates": [[[6.524, 33.1265], [16.88, -21.24]]], "type": "MultiLineString"}')
        self.assertEqual(self.mls2.__str__(),
                         '{"coordinates": [[[6.524, 33.1265], [16.88, -21.24]], '
                         '[[16.88, -21.24], [6.524, 33.1265]]], "type": "MultiLineString"}')
        self.assertEqual(self.mls3.__str__(),
                         '{"coordinates": [[[16.88, -21.24], [6.524, 33.1265]], '
                         '[[6.524, 33.1265], [16.88, -21.24]]], "type": "MultiLineString"}')
        self.assertEqual(self.mls4.__str__(),
                         '{"coordinates": [[[6.524, 33.1265], [16.88, -21.24]], '
                         '[[16.88, -21.24], [6.524, 33.1265]]], "type": "MultiLineString"}')
        self.assertEqual(self.mls5.__str__(),
                         '{"coordinates": [[[16.88, -21.24], [6.524, 33.1265]], '
                         '[[6.524, 33.1265], [16.88, -21.24]]], "type": "MultiLineString"}')
        self.assertEqual(self.mls6.__str__(),
                         '{"coordinates": [[[6.524, 33.1265], [16.88, -21.24]], '
                         '[[6.524, 33.1265], [16.88, -21.24]]], "type": "MultiLineString"}')


if __name__ == '__main__':
    unittest.main()
