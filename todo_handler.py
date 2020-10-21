#!/usr/bin/python
# !-*- coding:utf-8 -*-

from handler import Handler
import red_font_handler

"""
将读取的todo列表友好展示
输入: todo对象列表
输出: 带序号的todo列表字符串,如果是important的todo,则用红色表示
"""


class TodoHandler(Handler):

    def handle(self, msg, args=None):
        """
        msg一定是一个列表,数据结构可以到core.py查看,大概为[{"id": xxx, "content": "xxx"}]这个样子
        """
        if msg is None or type(msg) is not list:
            return msg

        rfh = red_font_handler.RedFontHandler()
        content = ""
        for todo in msg:
            current = "%s. %s" % (todo['id'], todo['content'])
            if todo.get('important') is not None and todo.get('important') > 0:
                current = rfh.handle(current)
            content = "%s%s\n" % (content, current)

        return content.strip()
