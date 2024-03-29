#!/usr/bin/python3
"""
    module for Base
"""


class Base:
    """
        class for Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new polygon object with the given id.

        Args:
            id (int): The id of this polygon object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
