#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Open/Closed Principle:
Software entities ... should be open for extension, but closed for modification.


Mix-ins:
Mix-in programming is a style of software development where units of functionality are created in a class and then mixed
in with other classes.

A mix-in is not the “primary” superclass of any given class, does not care what class it is used with, is used with many
classes scattered throughout the class hierarchy and is introduced dynamically at runtime.

Python provides an ideal language for mix-in development because it supports multiple inheritance, supports full-dynamic
binding and allows dynamic changes to classes


References:
    https://www.linuxjournal.com/article/4540
    https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful/20022860#20022860
"""


class NotComparableNumbersMixIn(object):
    """
    This class has methods which use `<=` and `==`,
    but this class does NOT implement those methods.

    It is possible to instantiate a mixin:
        o = ComparableNumbersMixin()
    but one of its methods raise an exception:
        o != o
    """

    def __eq__(self, other: object) -> bool:
        """
        Magic method for the inversion of the equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's equal return true.
        :rtype: bool
        """
        return not self.__getattribute__('number') == other.__getattribute__('number')

    def __ne__(self, other: object) -> bool:
        """
        Magic method for the inversion of the not equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's not equal return true.
        :rtype: bool
        """
        return not self.__getattribute__('number') != other.__getattribute__('number')

    def __le__(self, other: object) -> bool:
        """
        Magic method for the inversion of the less and equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's less and equal return true.
        :rtype: bool
        """
        return not self.__getattribute__('number') <= other.__getattribute__('number')

    def __lt__(self, other: object) -> bool:
        """
        Magic method for the inversion of the less than other operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's less than other return true.
        :rtype: bool
        """
        return not self.__getattribute__('number') < other.__getattribute__('number')

    def __ge__(self, other: object) -> bool:
        """
        Magic method for the inversion of the greater or equal operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's greater or equal return true.
        :rtype: bool
        """
        return not self.__getattribute__('number') >= other.__getattribute__('number')

    def __gt__(self, other: object) -> bool:
        """
        Magic method for the inversion of the greater than other operator.

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's greater than other return true.
        :rtype: bool
        """
        return not self.__getattribute__('number') > other.__getattribute__('number')
