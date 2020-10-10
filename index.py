#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
启动脚本
"""

import core
import const
import sys
import font_color
import os
import pipeline
import todo_handler


def init_workspace():
    """
    初始化todo工作空间和各个文件
    """
    if not os.path.exists(const.WORK_PATH):
        os.mkdir(const.WORK_PATH, 0o775)
    if not os.path.exists(const.TODO_FILE):
        file = open(const.TODO_FILE, "w")
        file.close()


def register_opts(argv):
    todo_pipeline = pipeline.Pipeline()
    handler = todo_handler.TodoHandler()
    todo_pipeline.add_handler(handler)

    opts = {}
    try:
        opts = core.get_opt(argv, "han:A:D:I:i:")
    except ValueError as e:
        print(font_color.COLOR_RED.font_color(str(e)))
        print(font_color.COLOR_RED.font_color(const.HINT))
        exit(2)

    if opts is None or len(opts) == 0:
        todo_list = core.read_todo()
        msg = todo_pipeline.handle(todo_list[-3:])
        print(msg)
        exit()

    for opt in opts.keys():
        if opt == '-h':
            print(const.HINT)
            exit()
        if opt == '-a':
            todo_list = core.read_todo()
            msg = todo_pipeline.handle(todo_list)
            print(msg)
            exit()
        if opt == '-n':
            todo_list = core.read_todo()
            msg = todo_pipeline.handle(todo_list[-opts[opt][0]:])
            print(msg)
            exit()
        if opt == '-A':
            core.add_todo(opts[opt][0])
            exit()
        if opt == '-D':
            core.del_item(opts[opt][0])
            exit()
        print(font_color.COLOR_RED.font_color(const.HINT))


def start(argv):
    """
    1. 初始化todo工作空间和各个文件
    2. 注册功能
    """
    init_workspace()
    register_opts(argv)


if __name__ == "__main__":
    start(sys.argv[1:])

