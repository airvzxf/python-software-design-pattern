#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SOLID

Open/Closed Principle: Mix-ins.

References:
    https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful/20022860#20022860
"""


class LogNumbersMixIn(object):
    """""
    Logs the name of the class.
    """""

    def log(self) -> None:
        """
        Logs the class taking the self instance.

        :rtype: None
        """
        print("Recording...")
        print("Class: ", self.__class__)
        print()

    def __eq__(self, other: object) -> bool:
        """
        Example to shows how this method is never called, except if this class is called first for example:

        ```python
            class InverseNumber(LogNumbersMixIn, NotComparableNumbersMixIn):
                pass
        ```

        :param other: The number which needs compare, it's not the self number.
        :type other: object

        :return: If it's equal return true.
        :rtype: bool
        """
        print("This method is never touch in this examples.")
        return False
