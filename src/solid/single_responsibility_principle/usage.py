#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Single responsibility principle.
A class should have only a single responsibility, that is, only changes to one part of the software's specification
should be able to affect the specification of the class.

Example of the implementation of the Rectangle and GeometricRectangle classes.

Execute:
```bash
PYTHONPATH=./../../ \
./../../venv/bin/python \
./usage.py
```

References:
    https://en.wikipedia.org/wiki/Single_responsibility_principle
    https://www.researchgate.net/publication/323935872
"""
from solid.single_responsibility_principle.classes.draw_rectangle import DrawRectangle
from solid.single_responsibility_principle.classes.geometric_rectangle import GeometricRectangle
from solid.single_responsibility_principle.classes.rectangle import Rectangle

if __name__ == '__main__':
    # This class only use one class and two methods area and draw.
    rectangle = Rectangle(width=10, height=5)
    print("area: ", rectangle.area())
    rectangle.draw()

    print("\n")

    # Applying the SRP we split the Rectangle functions and also created a new class for Drawing Geometric Rectangles.
    geometric_rectangle = GeometricRectangle(width=8, height=12)
    print("geometric_area: ", geometric_rectangle.area())
    draw_rectangle = DrawRectangle(geometric_rectangle)
    draw_rectangle.draw()
