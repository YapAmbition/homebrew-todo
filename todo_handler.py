#!/usr/bin/python
# !-*- coding:utf-8 -*-

from handler import Handler

"""
将读取的todo列表友好展示
输入: todo对象列表
输出: 带序号的todo列表字符串
"""


class TodoHandler(Handler):

    def handle(self, msg, args=None):
        """
        msg一定是一个列表,数据结构可以到core.py查看,大概为[{"id": xxx, "content": "xxx"}]这个样子
        """
        if msg is None or type(msg) is not list:
            return msg

        content = ""
        for todo in msg:
            content = "%s%s. %s\n" % (content, todo['id'], todo['content'])

        return content.strip()
