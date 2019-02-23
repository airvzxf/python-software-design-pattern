#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Single responsibility principle.
A class should have only a single responsibility, that is, only changes to one part of the software's specification
should be able to affect the specification of the class.

Split it in two classes GeometricRectangle and DrawRectangle.

References:
    Duncan Watson-Parris, Copyright Tessella 2013
"""


class GeometricRectangle:
    """
    Abstraction for the geometric rectangle; get the area.
    """

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
        Create a rectangle taking the width and the height parameters.

        :param width: Width of the rectangle.
        :type width: int

        :param height: Height of the rectangle.
        :type height: int

        :rtype: None
        """
        self.width = width
        self.height = height
        print("Created a Geometric Rectangle")

    def area(self) -> int:
        """
        Return the area of the rectangle based on width and height.

        :return: The area.
        :rtype: int
        """
        return self.width * self.height
