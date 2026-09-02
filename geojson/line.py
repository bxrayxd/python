"""
This is the Line Module.
We gave you some basic methods.
Please implement all the methods that says TODO!

author: Ziyad Alsaeed
email: zalsaeed@qu.edu.sa
"""

from typing import List, Union

from geo import Geo
from point import Point, MultiPoint


class LineString(Geo):
    """
    A LineString object is a list that can have two points.

    >>> str(LineString(Point(6.524, 33.1265), Point(16.88, -21.24)))
    '{"coordinates": [[6.524, 33.1265], [16.88, -21.24]], "type": "LineString"}'
    """

    def __init__(self, p1: Point, p2: Point):
        if p1 == p2:
            raise ValueError(f"To form a line {p1.__repr__()} and {p2.__repr__()} must be different!")
        self.p1 = p1
        self.p2 = p2

    def get_coordinate(self) -> str:
        """
        This method returns the coordinates of the line.
        :return: A string that contains the coordinates of the line.
        """
        return f"[{self.p1.get_coordinate()}, {self.p2.get_coordinate()}]"
        
    def is_linear_ring(self) -> bool:
        """
        A line can never be a linear ring as long as p1 != p2.
        :return: Boolean. Always returns False
        """
        return False

    def get_first_point(self) -> Point:
        return self.p1

    def get_last_point(self) -> Point:
        return self.p2

    def __repr__(self) -> str:
        return f"LineString({self.p1.__repr__()}, {self.p2.__repr__()})"

    def __str__(self):
        """
        This method returns the string representation of the line.
        :return: A string that contains the coordinates of the line.
        """
        return "{" + f'"coordinates": {self.get_coordinate()}, {self.type()}' + "}"


class MultiLineString(Geo):
    """

    >>> str(MultiLineString([LineString(Point(6.524, 33.1265), Point(16.88, -21.24))]))
    {"coordinates": [[[6.524, 33.1265], [16.88, -21.24]]], "type": "MultiLineString"}

    >>> str(MultiLineString([LineString(Point(6.524, 33.1265), Point(16.88, -21.24)), MultiPoint([Point(6.524, 33.1265), Point(16.88, -21.24)])]))
    {"coordinates": [[[6.524, 33.1265], [16.88, -21.24]], [[6.524, 33.1265], [16.88, -21.24]]], "type": "MultiLineString"}
    """

    def __init__(self, lines: List[Union[LineString, MultiPoint]]):
        self.lines = lines

    def get_coordinate(self):
        """
        This method returns the coordinates of the lines.
        :return: A string that contains the coordinates of the lines.
        """
        # Use list comprehension to extract each line's coordinate
        coords = [line.get_coordinate() for line in self.lines]
        return f"[{', '.join(coords)}]"

    def is_linear_ring(self):
        if not self.lines:
            return False
        else:
            return self.lines[0].get_first_point() == self.lines[-1].get_last_point()

    def get_first_point(self) -> Point:
        if self.lines:
            return self.lines[0].get_first_point()
        else:
            raise KeyError(f"No lines available '{self.lines}'")

    def get_last_point(self) -> Point:
        if self.lines:
            return self.lines[-1].get_last_point()
        else:
            raise KeyError(f"No lines available '{self.lines}'")

    def __repr__(self) -> str:
        return f"MultiLineString({self.lines})"

    def __str__(self):
        """
        This method returns the string representation of the lines.
        :return: A string that contains the coordinates of the lines.
        """
        return "{" + f'"coordinates": {self.get_coordinate()}, {self.type()}' + "}"
