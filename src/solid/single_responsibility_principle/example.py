#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Single responsibility principle.
A class should have only a single responsibility, that is, only changes to one part of the software's specification
should be able to affect the specification of the class.

Example of the implementation of the impure and pure classes.

Execute:
```bash
PYTHONPATH=./../../ \
./../../venv/bin/python \
./example.py
```
"""

from solid.single_responsibility_principle.classes.impure import Rectangle
from solid.single_responsibility_principle.classes.pure import GeometricRectangle, DrawRectangle

if __name__ == '__main__':
    rectangle = Rectangle(width=10, height=5)
    print("area: ", rectangle.area())
    rectangle.draw()

    print("\n")

    geometric_rectangle = GeometricRectangle(width=8, height=12)
    print("geometric_area: ", geometric_rectangle.area())
    draw_rectangle = DrawRectangle(geometric_rectangle)
    draw_rectangle.draw()
