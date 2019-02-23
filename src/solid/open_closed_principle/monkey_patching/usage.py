#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Open/Closed Principle: Mix-ins.
Software entities ... should be open for extension, but closed for modification..

A monkey patch is a way for a program to extend or modify supporting system software locally (affecting only the running
instance of the program).

In Python, we are able to change the functionality of any method, class or function at will. We can even add methods to
classes (or individual instances!) at run-time.

Execute:
```bash
PYTHONPATH=./../../ \
./../../venv/bin/python \
./usage.py
```
"""
from solid.open_closed_principle.monkey_patching.classes.geometric_rectangle import GeometricRectangle


def monkey_patching() -> None:
    """
    Monkey Patching function which will be add a function.
    It prints a message.

    :rtype: None
    """
    print("I'm always return an square taking the width, just because I'm a monkey.")


def monkey_patching_area(self: object) -> int:
    """
    Monkey Patching function which will be replace the area method.
    It returns the width powered by 2 as the squares.

    :param self: The Geometric Rectangle object.
    :type self: object

    :return: The area of the square taking the width.
    :rtype: int
    """
    return self.__getattribute__('width') ** 2


if __name__ == '__main__':
    geometric_rectangle = GeometricRectangle(width=8, height=12)
    print("geometric_area: ", geometric_rectangle.area())
    print()

    # Add a new function in the object.
    geometric_rectangle.monkey_patching = monkey_patching
    geometric_rectangle.monkey_patching()
    print()

    # Adding a function into the instanced object:
    # Throws an error if we try to override the object method with the runtime function.
    # TypeError: monkey_patching_area() missing 1 required positional argument: 'self'
    # Code:
    #   geometric_rectangle.area = monkey_patching_area
    #   print("geometric_area Monkeys: ", geometric_rectangle.area())
    #   print()

    # Replace the method with a runtime function.
    GeometricRectangle.area = monkey_patching_area
    geometric_monkey = GeometricRectangle(width=5, height=10)
    print("geometric_monkey: ", geometric_monkey.area())
    print()

    # You can also remove the new method
    del geometric_rectangle.monkey_patching
