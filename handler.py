#!/usr/bin/python
# !-*- coding:utf-8 -*-

import abc

"""
流水线执行者
"""


class Handler(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def handle(self, msg):
        pass

