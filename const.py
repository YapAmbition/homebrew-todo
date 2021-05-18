#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
常量包,只用于配置核心常量
"""

import os

# todo的帮助提示
HINT = """todo [-hanADiI] [args...]
todo        打印最近3条todo项
-h          获得帮助
-a          打印所有的todo
-n n        返回最后n条todo
-A arg      新增一条内通为arg的todo
-D n        删除第n条todo
-i [n]      将第n条标记为重要,不传参数时展示所有重要的todo
-I [n]      取消第n条的重要标记,不传参数时展示所有不重要的todo"""

# 默认返回几条todo项
TODO_COUNT = 3

# 用户家目录的绝对路径
HOME_PATH = os.path.expanduser('~')

# 工作路径的绝对路径
WORK_PATH = "%s/.todo" % HOME_PATH

# todo文件的绝对路径
TODO_FILE = "%s/todo_list" % WORK_PATH

LABEL_SIZE = 8
