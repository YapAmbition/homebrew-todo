#!/usr/bin/python
# !-*- coding:utf-8 -*-

import const
import json

"""
核心功能包
todo内容:
{
"id": xx,
"content": "xxx"
}
"""


def read_todo(from_index=None, to_index=None):
    """
    读取todo文件中下标在[from_index, to_index]之间的todo,如果todo总量不够则有多少返回多少
    :param from_index: 起始下标, 传入None表示从第一个开始返回
    :param to_index: 终止下标, 传入None表示返回到最后一个
    :return: todo列表
    """
    if from_index is None:
        from_index = 0
    if to_index is not None and to_index < from_index:
        return []

    file = open(const.TODO_FILE, "r")
    lines = file.readlines()
    file.close()
    content = ""
    if lines is not None and len(lines) > 0:
        content = "".join(lines)

    todo_items = []
    if lines != "" and len(lines) > 0:
        todo_items = json.loads(content)

    if to_index is None:
        to_index = len(todo_items) - 1

    return todo_items[from_index: to_index + 1]


def add_todo(item):
    """
    添加一条todo到todo列表
    :param item: todo内容
    """
    if item is None or len(item) == 0:
        return
    todo_list = read_todo(None, None)
    last_id = 0 if len(todo_list) == 0 else todo_list[-1]['id']
    todo_list.append({"id": last_id + 1, "content": item})
    file = open(const.TODO_FILE, "w")
    file.write(json.dumps(todo_list))
    file.close()


def del_item(indexes):
    """
    删除todo
    :param indexes: 待删除的下标
    """
    if indexes is None or len(indexes) == 0:
        return
    if type(indexes) is not list:
        indexes = [int(indexes)]

    todo_list = read_todo(None, None)
    new_todo_list = []
    no = 1
    for i in range(1, len(todo_list) + 1):
        if i not in indexes:
            todo_list[i-1]['id'] = no
            new_todo_list.append(todo_list[i-1])
            no = no + 1

    file = open(const.TODO_FILE, "w")
    file.write(json.dumps(new_todo_list))
    file.close()


def get_opt(args: list, opts: str):
    """
    传入参数列表,参数获取范式
    输入abc表示-a, -b, -c,后面都不跟参数
    输入ab:c::表示-a不跟参数,-b后面跟一个参数,-c后跟2个参数
    参数不够会用None来代替

    :param args: 传入的参数列表
    :param opts: 接收参数的范式,不能以':'开头,不能包含'-'
    :return: {opt:[], ...}
    """
    res = {}
    if args is None or len(args) == 0:
        return res
    if '-' in opts or opts.startswith(':'):
        raise ValueError("'-' is not a valid opt pattern and ':' can not at opts's begin")

    pattern = {}
    i = 0
    while i < len(opts):
        now = '-' + opts[i]
        pattern[now] = 0
        while i + 1 < len(opts) and opts[i + 1] == ':':
            i = i + 1
            pattern[now] = pattern[now] + 1
        i = i + 1

    i = 0
    while i < len(args):
        now_opt = args[i]
        if now_opt is None or not str(now_opt).startswith('-'):
            raise ValueError("opt must begin with '-'")
        params = []
        res[now_opt] = params
        param_count = pattern.get(str(now_opt))
        if param_count is None:
            raise ValueError("this opt is not declared: %s" % now_opt)
        for j in range(param_count):
            if i + 1 < len(args) and args[i + 1] is not None and not str(args[i + 1]).startswith('-'):
                i = i + 1
                params.append(args[i])
            else:
                params.append(None)
        i = i + 1
    return res
