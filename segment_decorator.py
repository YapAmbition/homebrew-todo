#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
段装饰器,用来标记每一条todo的样式
4个接口:
add_segment: 添加一段样式
read_segment: 读取from_segment到to_segment段的样式
update_segment: 更新一段样式
resize: 升级装饰器版本,增加每个segment的长度
"""

import os
import struct


class SegmentDecorator:
    """
    文件格式: 版本号(2字节) + 段
    可以很简单地得出第n段在文件中的位置
    """

    def __init__(self, filename, version=1):
        self.filename = filename
        self.version: int = version  # 版本
        self.version_byte = 2  # 版本字节数,写死
        self.__init_version()
        self.__init_style_file()

    def clear(self):
        """
        清除所有除version外的数据
        """
        self.__write_version()

    def __init_version(self):
        """
        初始化版本,版本头占的字节,段头占的字节
        """
        # 版本号: 段字节数
        self.__version_declare = {
            1: 1
        }
        segment_byte = self.__version_declare.get(self.version)
        if segment_byte is None:
            raise ValueError("version [%s] haven't declared" % self.version)
        self.segment_byte = segment_byte

    def resize(self):
        """
        重新定义版本号大小和每段的大小
        新版本的版本号和每段大小必须大于旧版本
        新旧版本都必须定义在self.__version_declare中,且格式必须相同
        """
        origin_version = self.__read_version()
        now_version = self.version
        if origin_version == now_version:
            raise ValueError("can not resize because version have no change")
        if now_version < origin_version:
            raise ValueError("version can not less than before")
        before_segment_byte = self.__version_declare.get(origin_version)
        now_segment_byte = self.__version_declare.get(now_version)
        if now_segment_byte is None:
            raise ValueError("version [%s] declare is missing" % now_version)
        if now_segment_byte < before_segment_byte:
            raise ValueError("segment_byte can not less than before")
        self.segment_byte = before_segment_byte  # 要读原来的数据就要把segment_byte换为旧的
        segment_list = self.read_segment(0, self.segment_size() - 1)
        self.segment_byte = now_segment_byte  # 再把segment_byte换为新的
        self.__write_version()
        self.add_segments(segment_list)

    def __adjust_byte(self, num: int):
        """
        将传入的数字转化为字节
        :return: 字节
        """
        if num is None:
            raise ValueError("num can not be null")
        num = int(num)
        if num not in range(0, 1 << (self.segment_byte * 8)):
            raise ValueError("num can not cast to byte by %s byte" % self.segment_byte)
        return num.to_bytes(self.segment_byte, "big")

    def __is_exists(self):
        """
        文件是否存在
        :return: 是否存在
        """
        if self.filename is None:
            return False
        return os.path.exists(self.filename)

    def __write_version(self):
        """
        写入版本段
        """
        file = open(self.filename, "wb")
        file.write(self.version.to_bytes(self.version_byte, "big"))
        file.close()

    def __init_style_file(self):
        """
        初始化decorator文件
        在文件中写入版本和每段长度
        """
        if self.filename is None:
            raise IOError("filename is None!")
        if not self.__is_exists():
            self.__write_version()

    def add_segments(self, segments: list):
        """
        添加一些segment
        :param segments: segment列表,每个segment必须是正整数,且二进制长度不得超过self.segment_length
        """
        if segments is None or len(segments) == 0:
            raise ValueError("segments can not be null")
        list(segments)
        for segment in segments:
            try:
                segment = int(segment)
            except TypeError:
                raise TypeError("segment's type must be int")
            if segment < 0:
                raise ValueError("segment can not must >= 0")

        file = open(self.filename, "ab")
        if file is None:
            raise IOError("file is not exists, filename: %s" % self.filename)
        for segment in segments:
            segment = int(segment)
            file.write(self.__adjust_byte(segment))
        file.close()

    def __parse_seg_bytes(self, seg_bytes):
        """
        解析struct解析字节返回的数组
        :param seg_bytes: struct解析字节返回的数组
        :return: 数组代表的整数
        """
        res = 0
        for i in range(self.segment_byte):
            res = res + seg_bytes[self.segment_byte - 1 - i] * (256 ** i)
        return res

    def read_segment(self, from_segment: int = 0, to_segment: int = 0):
        """
        读取文件的段
        :param from_segment: 从第几段读取(包含),从0开始
        :param to_segment: 读到第几段(包含),从0开始
        :return: 段的十进制值列表
        """
        if self.segment_size() < 1:
            return []
        res = []
        from_segment = int(from_segment)
        to_segment = int(to_segment)
        if from_segment < 0 or to_segment < 0 or from_segment > to_segment:
            return res
        file = open(self.filename, "rb")
        file.seek(self.version_byte + from_segment * self.segment_byte)  # 定位到from_segment的位置
        for i in range(to_segment - from_segment + 1):
            byte_info = file.read(self.segment_byte)
            if byte_info is None or len(byte_info) == 0:
                raise ValueError("there is no such many segment")
            seg_bytes = struct.unpack("%dB" % self.segment_byte, byte_info)
            segment = self.__parse_seg_bytes(seg_bytes)
            res.append(segment)
        file.close()
        return res

    def __read_version(self):
        """
        返回版本字节
        :return: 版本段
        """
        file = open(self.filename, "rb")
        byte_info = file.read(self.version_byte)
        if byte_info is None or len(byte_info) == 0:
            raise ValueError("there is no such many segment")
        version_byte = struct.unpack("%dB" % self.version_byte, byte_info)
        file.close()
        return self.__parse_seg_bytes(version_byte)

    def segment_size(self):
        """
        返回文件有多少段
        :return: 文件有多少segment
        """
        size_char = os.path.getsize(self.filename)
        if size_char <= self.version_byte:
            return 0
        size_char = size_char - self.version_byte
        size = size_char / self.segment_byte
        size = int(size)
        return size

    def update_segment(self, n, segment):
        """
        更新段
        :param n: 第n段,从0开始
        :param segment: 更新后的值
        """
        n = int(n)
        segment = int(segment)
        segment_size = self.segment_size()
        if n not in range(0, segment_size):
            raise ValueError("can not find segment at index: %s" % n)
        segment_list = self.read_segment(0, self.segment_size() - 1)
        segment_list[n] = segment
        self.__write_version()
        self.add_segments(segment_list)
