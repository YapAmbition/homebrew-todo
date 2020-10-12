#!/usr/bin/python
# !-*- coding:utf-8 -*-

from handler import Handler

"""
返回有特定标签的todo对象列表
输入: todo对象列表
输出: 带特定label的todo对象列表
"""


class LabelHandler(Handler):

    def handle(self, msg, args=None):
        """
        msg一定是一个列表,数据结构可以到core.py查看,大概为[{"id": xxx, "content": "xxx", "label": []}]这个样子
        :arg 指定的label
        """
        if msg is None or type(msg) is not list:
            return msg

        label = args
        label_list = []
        if label is None:
            return label_list

        for todo in msg:
            if todo.get('label') is not None:
                labels = todo.get('label')
                if str(label) in labels:
                    label_list.append(todo)
        return label_list
