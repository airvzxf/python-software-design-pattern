#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Open/Closed Principle: Mix-ins.

References:
    https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful/20022860#20022860
"""
from solid.open_closed_principle.mixins.classes.log_numbers_mixin import LogNumbersMixIn
from solid.open_closed_principle.mixins.classes.numbers_mixin import NotComparableNumbersMixIn


class InverseNumber(NotComparableNumbersMixIn, LogNumbersMixIn):
    """
    Create a number and add the inverse equality also logs the creation of the class.
    """

    def __init__(self, number: object) -> None:
        """
        Init the class.

        :param number: The Number.
        :type number: object

        :rtype: None
        """
        self.log()
        self.number = number
