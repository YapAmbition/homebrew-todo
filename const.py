#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
常量包
"""

# todo的帮助提示
HINT = """todo [-hanAdD] [args...]
todo        打印最近3条todo项
-h          获得帮助
-a          打印所有的todo
-n arg      返回最后arg条todo
-A arg      新增一条内通为arg的todo
-d          删除最后一条todo
-D          删除第n条todo"""

# todo的列表文件名
TODO_FILE_NAME = "todo_list"

# todo的文件夹名
TODO_DIR_NAME = ".todo"

# 默认返回几条todo项
TODO_COUNT = 3
