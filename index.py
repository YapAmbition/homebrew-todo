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
from important_pipeline import ImportantPipeline
from unimportant_pipeline import UnimportantPipeline
from todo_pipeline import TodoPipeline
from label_pipeline import LabelPipeline


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
    todo_pipeline = TodoPipeline()
    important_pipeline = ImportantPipeline()
    unimportant_pipeline = UnimportantPipeline()
    label_pipeline = LabelPipeline()

    opts = {}
    try:
        opts = core.get_opt(argv, "han:A:D:I:i:l::L::")
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
            if opts[opt][0] is not None:
                todo_list = core.read_todo()
                msg = todo_pipeline.handle(todo_list[-int(opts[opt][0]):])
                print(msg)
                exit()
            else:
                todo_list = core.read_todo()
                msg = todo_pipeline.handle(todo_list[-3:])
                print(msg)
                exit()
        if opt == '-A':
            core.add_todo(opts[opt][0])
            exit()
        if opt == '-D':
            core.del_item(opts[opt][0])
            exit()
        if opt == '-i':
            if opts[opt][0] is None:
                todo_list = core.read_todo()
                msg = important_pipeline.handle(todo_list)
                print(msg)
                exit()
            else:
                core.important(opts[opt][0])
                exit()
        if opt == '-I':
            if opts[opt][0] is None:
                todo_list = core.read_todo()
                msg = unimportant_pipeline.handle(todo_list)
                print(msg)
                exit()
            else:
                core.unimportant(opts[opt][0])
                exit()
        if opt == '-l':
            if opts[opt][0] is not None:
                if opts[opt][1] is not None:
                    core.add_label(int(opts[opt][0]), str(opts[opt][1]))
                    exit()
                if opts[opt][1] is None:
                    todo_list = core.read_todo()
                    msg = label_pipeline.handle(todo_list, opts[opt][0])
                    print(msg)
                    exit()
        if opt == '-L':
            if opts[opt][0] is not None:
                if opts[opt][1] is not None:
                    core.del_label(int(opts[opt][0]), str(opts[opt][1]))
                    exit()
                if opts[opt][1] is None:
                    todo_list = core.read_todo()
                    msg = label_pipeline.handle(todo_list, str(opts[opt][0]))
                    print(msg)
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

