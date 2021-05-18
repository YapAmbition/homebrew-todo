#!/usr/bin/python
# !-*- coding:utf-8 -*-

from handler import Handler

"""
只返回不重要的todo
输入: todo对象列表
输出: 重要的todo对象列表
"""


class UnimportantHandler(Handler):

    def handle(self, msg, args=None):
        """
        msg一定是一个列表,数据结构可以到core.py查看,大概为[{"id": xxx, "content": "xxx", "important": x}]这个样子
        """
        if msg is None or type(msg) is not list:
            return msg

        unimportant_list = []
        for todo in msg:
            if todo.get('important') is None or todo['important'] == 0:
                unimportant_list.append(todo)
        return unimportant_list

