#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Open/Closed Principle: Mix-ins.
Software entities ... should be open for extension, but closed for modification..

Mix-ins:
A mixin is a class such that some method of the class uses a method which is not defined in the class.
A mixin is a special kind of multiple inheritance. There are two main situations where mixin's are used:
* You want to provide a lot of optional features for a class.
* You want to use one particular feature in a lot of different classes.

The delineation between using true inheritance and using mixin's is nuanced, but it comes down to the fact that a mixin
is independent enough that it doesn't feel the same as a parent class.
Mixin's aren't generally used on their own, but aren't abstract classes either.

References:
    https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556
    https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful/36222493#36222493
    https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful/20022860#20022860
"""
from solid.open_closed_principle.mixins.classes.anti_number import AntiNumber
from solid.open_closed_principle.mixins.classes.number import Number

if __name__ == '__main__':
    assert (Number(5) == Number(5)) is True
    assert (Number(2) == Number(8)) is False
    assert (AntiNumber(5) == AntiNumber(5)) is False
    assert (AntiNumber(2) == AntiNumber(8)) is True

    assert (Number(5) != Number(10)) is True
    assert (Number(5) != Number(5)) is False
    assert (AntiNumber(5) != AntiNumber(10)) is False
    assert (AntiNumber(5) != AntiNumber(5)) is True

    assert (Number(1) < Number(10)) is True
    assert (Number(5) < Number(5)) is False
    assert (Number(10) < Number(1)) is False
    assert (AntiNumber(1) < AntiNumber(10)) is False
    assert (AntiNumber(5) < AntiNumber(5)) is True
    assert (AntiNumber(10) < AntiNumber(1)) is True

    assert (Number(1) <= Number(10)) is True
    assert (Number(5) <= Number(5)) is True
    assert (Number(10) <= Number(1)) is False
    assert (AntiNumber(1) <= AntiNumber(10)) is False
    assert (AntiNumber(5) <= AntiNumber(5)) is False
    assert (AntiNumber(10) <= AntiNumber(1)) is True

    assert (Number(10) > Number(1)) is True
    assert (Number(5) > Number(5)) is False
    assert (Number(1) > Number(10)) is False
    assert (AntiNumber(10) > AntiNumber(1)) is False
    assert (AntiNumber(5) > AntiNumber(5)) is True
    assert (AntiNumber(1) > AntiNumber(10)) is True

    assert (Number(10) >= Number(1)) is True
    assert (Number(5) >= Number(5)) is True
    assert (Number(1) >= Number(10)) is False
    assert (AntiNumber(10) >= AntiNumber(1)) is False
    assert (AntiNumber(5) >= AntiNumber(5)) is False
    assert (AntiNumber(1) >= AntiNumber(10)) is True
