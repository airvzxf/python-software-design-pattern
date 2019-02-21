#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Open/Closed Principle: Mix-ins.

References:
    https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful/20022860#20022860
"""
from solid.open_closed_principle.mixins.classes.log_numbers_mixin import LogNumbersMixIn


class Number(LogNumbersMixIn):
    """
    Create an number and add the equality also logs the creation of the class.
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

    def __eq__(self, other: object) -> bool:
        """
        Magic method for equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's equal return true.
        :rtype: bool
        """
        return self.number == other

    def __ne__(self, other: object) -> bool:
        """
        Magic method for not equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's not equal return true.
        :rtype: bool
        """
        return self.number != other

    def __le__(self, other: object) -> bool:
        """
        Magic method for less and equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's less and equal return true.
        :rtype: bool
        """
        return self.number <= other

    def __lt__(self, other: object) -> bool:
        """
        Magic method for less than other operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's less than other return true.
        :rtype: bool
        """
        return self.number <= other and (self.number != other)

    def __ge__(self, other: object) -> bool:
        """
        Magic method for greater or equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's greater or equal return true.
        :rtype: bool
        """
        return self.number == other or self.number > other

    def __gt__(self, other: object) -> bool:
        """
        Magic method for greater than other operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's greater than other return true.
        :rtype: bool
        """
        return not self.number <= other
