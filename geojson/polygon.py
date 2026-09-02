"""
This is the Point Module.
We gave you some basic methods.
Please implement all the methods that says TODO!

We don't check for right-hand orientation as explained on:
https://datatracker.ietf.org/doc/html/rfc7946#appendix-B
Thus, if not used carefully, this application can generate
some non-rendering polygons.

author: Ziyad Alsaeed
email: zalsaeed@qu.edu.sa
"""

from typing import List

from geo import Geo
from point import Point, MultiPoint
from line import MultiLineString


class Polygon(Geo):
    """

    >>> str(Polygon(MultiLineString([MultiPoint([Point(2.38, 57.322), Point(-120.43, 19.15), Point(23.194, -20.28),
    >>> Point(2.38, 57.322)])])))
    {"coordinates": [[[2.38, 57.322], [-120.43, 19.15], [23.194, -20.28], [2.38, 57.322]]], "type": "Polygon"}

    >>> str(Polygon(MultiLineString([MultiPoint([Point(0, 0), Point(10, 0), Point(10, 10), Point(0, 10),
    >>> Point(0, 0)])])))
    {"coordinates": [[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]], "type": "Polygon"}
    """
    def __init__(self, polygon: MultiLineString):
        if not polygon.is_linear_ring():
            raise ValueError(f"The {polygon.__repr__()} given is not a linear ring.")
        self.polygon = polygon

    def get_coordinate(self):
        """
        This method returns the coordinates of the polygon.
        :return: A string that contains the coordinates of the polygon.
        """
        # Use list comprehension to extract each line's coordinate
        coords = [line.get_coordinate() for line in self.polygon.lines]
        return f"[{', '.join(coords)}]"

    def is_linear_ring(self) -> bool:
        return self.polygon.is_linear_ring()

    def get_first_point(self) -> Point:
        return self.polygon.get_first_point()

    def get_last_point(self) -> Point:
        return self.polygon.get_last_point()

    def __repr__(self) -> str:
        return f"Polygon({self.polygon.__repr__()})"

    def __str__(self) -> str:
        """
        This method returns the string representation of the polygon.
        :return: A string that contains the coordinates of the polygon.
        """
        return "{" + f'"coordinates": {self.get_coordinate()}, {self.type()}' + "}"


class MultiPolygon(Geo):
    """

    All one line!
    >>> str(MultiPolygon([Polygon(MultiLineString([MultiPoint([Point(0, 0), Point(10, 0), Point(10, 10),
    >>> Point(0, 10), Point(0, 0)])])),
    >>> Polygon(MultiLineString([MultiPoint([Point(11, 11), Point(14, 11), Point(14, 14), Point(11, 14),
    >>> Point(11, 11)])])),
    >>> Polygon(MultiLineString([MultiPoint([Point(1, 1), Point(4, 1), Point(4, 4), Point(1, 4), Point(1, 1)])]))]))

    {"coordinates": [
        [[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]],
        [[[11, 11], [14, 11], [14, 14], [11, 14], [11, 11]]],
        [[[1, 1], [4, 1], [4, 4], [1, 4], [1, 1]]]
    ], "type": "MultiPolygon"}
    """

    def __init__(self, polygons: List[Polygon]):
        if not all(p.is_linear_ring() for p in polygons):
            raise ValueError(f"One of the polygons is not a linear ring  {polygons}.")
        self.polygons = polygons

    def get_coordinate(self):
        """
        This method returns the coordinates of the polygons.
        :return: A string that contains the coordinates of the polygons.
        """
        # Use list comprehension to extract each polygon's coordinate
        coords = [polygon.get_coordinate() for polygon in self.polygons]
        return f"[{', '.join(coords)}]"

    def is_linear_ring(self) -> bool:
        return all(p.is_linear_ring() for p in self.polygons)

    def __repr__(self) -> str:
        return f"MultiPolygon({self.polygons})"

    def __str__(self):
        """
        This method returns the string representation of the polygons.
        :return: A string that contains the coordinates of the polygons.
        """
        return "{" + f'"coordinates": {self.get_coordinate()}, {self.type()}' + "}"
