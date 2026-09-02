"""
This is the Point Module.
We gave you some basic methods.
Please implement all the methods that says TODO!

author: Ziyad Alsaeed
email: zalsaeed@qu.edu.sa
"""

from typing import List

from geo import Geo


class Point(Geo):
    """

    >>> str(Point(-115.81, 37.24))
    {"coordinates": [-115.81, 37.24], "type": "Point"}
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_coordinate(self) -> str:
        return f"[{self.x}, {self.y}]"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        """
        This is a base case!
        """
        return "{" + f'"coordinates": {self.get_coordinate()}, {self.type()}' + "}"


class MultiPoint(Geo):
    """
    A MultiPoints object is a list that can have multiple points.

    >>> str(MultiPoint([Point(5.2, 3.4), Point(-1.4, 2.5)]))
    {"coordinates": [[5.2, 3.4], [-1.4, 2.5]], "type": "MultiPoint"}
    """

    def __init__(self, points: List[Point]):
        self.points = points

    def get_coordinate(self):
        # Use list comprehension to extract each point's coordinate
        coords = [f"[{p.x}, {p.y}]" for p in self.points]
        return f"[{', '.join(coords)}]"

    def is_linear_ring(self):
        if not self.points:
            return False
        else:
            return self.points[0] == self.points[-1]

    def get_first_point(self) -> Point:
        if self.points:
            return self.points[0]
        else:
            raise KeyError(f"No points available '{self.points}'")

    def get_last_point(self) -> Point:
        if self.points:
            return self.points[-1]
        else:
            raise KeyError(f"No points available '{self.points}'")

    def __repr__(self) -> str:
        return f"MultiPoint({self.points})"

    def __str__(self):
        return "{" + f'"coordinates": {self.get_coordinate()}, {self.type()}' + "}"