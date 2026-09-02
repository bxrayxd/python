"""
This is the Geo Module.

author: Ziyad Alsaeed
email: zalsaeed@qu.edu.sa
"""


class Geo:

    def __init__(self):
        raise NotImplementedError(f"Not Implemented on {self.__class__.__name__}")

    def get_coordinate(self) -> str:
        raise NotImplementedError(f"Not Implemented on {self.__class__.__name__}")

    def is_linear_ring(self) -> bool:
        raise NotImplementedError(f"Not Implemented on {self.__class__.__name__}")

    def get_first_point(self):
        raise NotImplementedError(f"Not Implemented on {self.__class__.__name__}")

    def get_last_point(self):
        raise NotImplementedError(f"Not Implemented on {self.__class__.__name__}")

    def type(self) -> str:
        return f'"type": "{self.__class__.__name__}"'
