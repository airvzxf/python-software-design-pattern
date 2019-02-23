#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Open/Closed Principle:

References:
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
