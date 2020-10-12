#!/usr/bin/python
# !-*- coding:utf-8 -*-


from handler import Handler
import font_color

"""
输入: 字符串
输出: 能在终端展示为红色的字符串
"""


class RedFontHandler(Handler):

    def handle(self, msg, args=None):
        return font_color.COLOR_RED.font_color(msg)