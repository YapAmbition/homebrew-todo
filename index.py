#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
启动脚本
"""

import core
import const
import sys
import font_color
import style


def start(argv):
    home_path = core.get_home_path()
    work_path = "%s/%s" % (home_path, const.TODO_DIR_NAME)
    todo_file = "%s/%s" % (work_path, const.TODO_FILE_NAME)
    core.create_dir(work_path)
    core.create_file(todo_file)

    todo_style = style.Style(todo_file, work_path)  # 样式文件

    opts = {}
    try:
        opts = core.get_opt(argv, "han:A:D:I:i:")
    except ValueError as e:
        print(font_color.COLOR_RED.font_color(str(e)))
        print(font_color.COLOR_RED.font_color(const.HINT))
        exit(2)

    if opts is None or len(opts) == 0:
        print(core.read_tail(todo_file, const.TODO_COUNT))
        exit()

    for opt in opts.keys():
        if opt == '-h':
            print(const.HINT)
            exit()
        if opt == '-a':
            print(core.read_tail(todo_file))
            exit()
        if opt == '-n':
            print(core.read_tail(todo_file, opts[opt][0]))
            exit()
        if opt == '-A':
            core.add_item(todo_file, opts[opt][0])
            exit()
        if opt == '-D':
            if opts[opt][0] is None:
                core.del_item(todo_file)
            else:
                core.del_item(todo_file, opts[opt][0])
            exit()
        if opt == '-i':
            if opts[opt][0] is None:
                content = font_color.COLOR_GREEN.font_color(todo_style.get_important())
                if content is not None:
                    print(content)
            else:
                todo_style.mark_important(int(opts[opt][0]) - 1)
            exit()
        if opt == '-I':
            if opts[opt][0] is None:
                content = font_color.COLOR_GREEN.font_color(todo_style.get_important())
                if content is not None:
                    print(content)
            else:
                todo_style.unmark_important(int(opts[opt][0]) - 1)
            exit()
        print(font_color.COLOR_RED.font_color(const.HINT))


if __name__ == "__main__":
    start(sys.argv[1:])

