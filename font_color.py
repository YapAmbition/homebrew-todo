#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
可以通过font_color让字符串在终端中显示为有颜色的字
"""


class Color:
    def __init__(self, code: int):
        self.__code = code

    def font_color(self, msg):
        if msg is None or len(msg) == 0:
            return None
        return "\033[%dm%s\033[0m" % (self.__code, msg)


COLOR_BLACK = Color(30)
COLOR_RED = Color(31)
COLOR_GREEN = Color(32)
COLOR_YELLOW = Color(33)
COLOR_BLUE = Color(34)
COLOR_FONT_PURPLE = Color(35)
COLOR_FONT_SKY_BLUE = Color(36)
COLOR_FONT_WHITE = Color(37)
