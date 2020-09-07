#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
核心功能包
"""
import os


#   创建目录
#   如果目录不存在则创建目录
def create_dir(dir_name):
    exists = os.path.exists(dir_name)
    if not exists:
        os.mkdir(dir_name, 0o775)


#   创建文件
#   如果目录不存在则创建文件
def create_file(filename):
    exists = os.path.exists(filename)
    if not exists:
        file = open(filename, "w")
        file.close()


#   获取当前用户的家目录
def get_home_path():
    return os.path.expanduser('~')


#   判断传入对象是否是整形数字
def is_int(s):
    try:
        int(s)
        return True
    except TypeError or ValueError:
        return False


#   读取文件的最后几行
#   filename: 文件名
#   row_count: 读取行数,当row_count<0时读取整个文件
def read_tail(filename, row_count=-1):
    if not is_int(row_count):
        raise TypeError("row_count should be a number")
    row_count = int(row_count)
    file = open(filename, "r")
    if file is None:
        raise IOError("cant find this file: %s" % filename)
    lines = file.readlines()
    size = len(lines)
    if row_count < 0:
        row_count = size
    content = ''
    for i in range(1, size + 1):
        if i > (size - row_count):
            content = "%s%s. %s" % (content, i, lines[i - 1])
    file.close()
    return content.strip('\n')


def read(filename, nums):
    """
    读取第num行,num从1开始
    :param filename: 文件名
    :param nums: 行号列表(从1开始)
    :return: 数据列表,含行号
    """
    if filename is None:
        return []
    if is_int(nums):
        nums = [nums]
    if not isinstance(nums, type([])):
        raise ValueError("nums must be number or list")
    file = open(filename, "r")
    if file is None:
        raise IOError("cant find this file: %s" % filename)
    res = []
    lines = file.readlines()
    for i in range(len(nums)):
        if nums[i] in range(1, len(lines) + 1):
            res.append("%s. %s" % (nums[i], lines[nums[i] - 1]))
    return res


#   添加一条todo到文件末尾
#   filename:  文件名
#   item: 添加的todo
def add_item(filename, item):
    if filename is None or item is None or len(item) == 0: return
    file = open(filename, "a")
    if file is None:
        raise IOError("cant find this file: %s" % filename)
    item = item.strip()
    item = item + "\n"
    file.write(item)
    file.close()


#   删除一条todo
#   filename: 文件名
#   line: 行号,line <= 0时删除最后一条
def del_item(filename, line=0):
    if filename is None:
        return
    if not is_int(line):
        raise TypeError("line should be a number")
    line = int(line)
    file_r = open(filename, "r")
    if file_r is None:
        raise IOError("cant find this file: %s" % filename)
    lines = file_r.readlines()
    file_r.close()
    line_index = -1 if line <= 0 else line - 1
    if line_index >= len(lines):
        return None
    item = lines.pop(line_index)
    file_w = open(filename, "w")
    file_w.writelines(lines)
    file_w.close()
    return item


# 传入参数列表,参数获取范式
# args: 传入的参数列表
# opts: 接收参数的范式,不能以':'开头,不能包含'-'.
# 输入abc表示-a, -b, -c,后面都不跟参数
# 输入ab:c::表示-a不跟参数,-b后面跟一个参数,-c后跟2个参数
# 参数不够会用None来代替
# 返回{opt:[], ...}
def get_opt(args: list, opts: str):
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
