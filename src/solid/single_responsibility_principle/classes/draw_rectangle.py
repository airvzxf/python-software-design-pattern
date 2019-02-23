#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Single responsibility principle.

Split it in two classes GeometricRectangle and DrawRectangle.

References:
    Duncan Watson-Parris, Copyright Tessella 2013
"""


class DrawRectangle:
    """
    Draw a geometric rectangle.
    """
    from solid.single_responsibility_principle.classes.geometric_rectangle import GeometricRectangle

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
