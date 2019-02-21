#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Single responsibility principle.
A class should have only a single responsibility, that is, only changes to one part of the software's specification
should be able to affect the specification of the class.

Split it in two classes GeometricRectangle and DrawRectangle.

References:
Duncan Watson-Parris
Copyright Tessella 2013
"""

from solid.single_responsibility_principle.classes.geometric_rectangle import GeometricRectangle


class DrawRectangle:
    """
    Draw a geometric rectangle.
    """

    def __init__(self, rectangle: GeometricRectangle) -> None:
        """
        Create a draw object with a rectangle.

        :param rectangle: Geometric rectangle object.
        :type rectangle: GeometricRectangle

        :rtype: None
        """
        self.rectangle = rectangle
        print("Created a Draw Rectangle")

    def draw(self) -> None:
        """
        Draw the rectangle.

        :rtype: None
        """
        print("Drawing rectangle %ix%i" % (self.rectangle.width, self.rectangle.height))
        pass
