"""
This is the GeoCollection Module.
We gave you some basic methods.
Please implement all the methods that says TODO!

author: Ziyad Alsaeed
email: zalsaeed@qu.edu.sa
"""

from typing import List, Union

from geo import Geo
from point import Point, MultiPoint
from line import LineString, MultiLineString
from polygon import Polygon, MultiPolygon


class GeometryCollection(Geo):
    """


    >>> p1 = Point(1, 1)
    >>> p2 = Point(3, 3)
    >>> p3 = Point(1, 6)
    >>> line = LineString(p1, p2)
    >>> ml = MultiLineString([MultiPoint([p1, p2, p3])])
    >>> geo_collection = GeometryCollection([p1, p2, p3, line, ml])
    >>> str(geo_collection)

    {"geometries":
        [
            {"coordinates": [1, 1], "type": "Point"},
            {"coordinates": [3, 3], "type": "Point"},
            {"coordinates": [1, 6], "type": "Point"},
            {"coordinates": [[1, 1], [3, 3]], "type": "LineString"},
            {"coordinates": [[[1, 1], [3, 3], [1, 6]]], "type": "MultiLineString"}
        ],
    "type": "GeometryCollection"}
    """

    def __init__(self, collection: List[Union[Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon]]):
        self.collection = collection

    def __repr__(self) -> str:
        return f"GeometryCollection({self.collection})"

    def __str__(self):
        return f'{{"geometries": [{", ".join([str(geo) for geo in self.collection])}], "type": "GeometryCollection"}}'
