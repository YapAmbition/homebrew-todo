#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
启动脚本
"""

import core
import const
import sys
import getopt
import font_color


def start(argv):
    home_path = core.get_home_path()
    work_path = "%s/%s" % (home_path, const.TODO_DIR_NAME)
    todo_file = "%s/%s" % (work_path, const.TODO_FILE_NAME)
    core.create_dir(work_path)
    core.create_file(todo_file)

    opts = []
    try:
        opts, args = getopt.getopt(argv, "han:A:dD:")
    except getopt.GetoptError:
        print(const.HINT)
        exit(2)

    if opts is None or len(opts) == 0:
        print(core.read_tail(todo_file, const.TODO_COUNT))
        exit()

    for opt, arg in opts:
        if opt == '-h':
            print(font_color.COLOR_RED.font_color(const.HINT))
            exit()
        if opt == '-a':
            print(core.read_tail(todo_file))
            exit()
        if opt == '-n':
            print(core.read_tail(todo_file, arg))
            exit()
        if opt == '-A':
            if arg is None or len(arg) == 0:
                print(const.HINT)
            else:
                core.add_item(todo_file, arg)
            exit()
        if opt == '-D':
            core.del_item(todo_file, arg)
            exit()
        if opt == '-d':
            core.del_item(todo_file)
            exit()
        print(font_color.COLOR_RED.font_color(const.HINT))


if __name__ == "__main__":
    start(sys.argv[1:])

