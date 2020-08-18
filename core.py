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


#   读取文件的最后几行
#   filename: 文件名
#   row_count: 读取行数,当row_count<0时读取整个文件
def read_tail(filename, row_count=-1):
    if row_count is None or not str(row_count).isdigit():
        raise TypeError("row_count should be a number")
    row_count = int(row_count)
    file = open(filename)
    if file is None:
        raise IOError("cant find this file: %s" % filename)
    lines = file.readlines()
    size = len(lines)
    if row_count < 0:
        row_count = size
    content = ''
    for i in range(1, size + 1):
        if i > (size - row_count):
            content = "%s%s. %s" % (content, i, lines[i-1])
    file.close()
    return content.strip('\n')


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
    if not str(line).isdigit():
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

