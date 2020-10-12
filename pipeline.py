#!/usr/bin/python
# !-*- coding:utf-8 -*-

from handler import Handler

"""
流水线类,创建流水线类,往流水线中添加继承于Handler的handlers
"""


class Pipeline:

    def __init__(self):
        self.__handlers = []

    def handle(self, msg, args=None):
        for handler in self.__handlers:
            msg = handler.handle(msg, args)
        return msg

    def add_handler(self, handler: Handler):
        self.__handlers.append(handler)
