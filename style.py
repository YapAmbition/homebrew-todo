#!/usr/bin/python
# !-*- coding:utf-8 -*-

"""
样式配置
version: 1
每段长度: 1byte
从右往左数,第1bit: 1-重要,2-不重要
"""

import segment_decorator
import core


class Style:

    def __init__(self, todo_filename, work_path):
        self.todo_filename = todo_filename
        self.style_file = "%s/%s" % (work_path, "style.cfg")
        self.sd = segment_decorator.SegmentDecorator(self.style_file, version=1)
        self.__init_styles()

    def __init_styles(self):
        segment = core.read_tail(self.todo_filename, 1)
        if segment is not None and len(segment) > 0:
            num_s = segment.split(".")[0]
            num = int(num_s)
            if num != self.sd.segment_size():
                self.sd.clear()
                self.sd.add_segments([0] * num)

    def mark_important(self, num):
        """
        标记第num条为重要的todo(从0开始算)
        """
        if num is None or num < 0:
            return
        segments = self.sd.read_segment(num, num)
        if segments is not None and len(segments) == 1:
            segment = int(segments[0])
            segment |= 1
            self.sd.update_segment(num, segment)

    def unmark_important(self, num):
        """
        标记第num条为重要todo(从0开始计算)
        """
        if num is None or num < 0:
            return
        segments = self.sd.read_segment(num, num)
        if segments is not None and len(segments) == 1:
            segment = int(segments[0])
            segment &= 0
            self.sd.update_segment(num, segment)

    def get_important(self):
        """
        获取重要的todo
        """
        segments = self.sd.read_segment(0, self.sd.segment_size() - 1)
        if segments is not None and len(segments) > 0:
            important_nums = []
            for i in range(len(segments)):
                if segments[i] & 1 == 1:
                    important_nums.append(i + 1)  # 这里一定要从1开始,因为后面的接口就是从1开始的
            todos = core.read(self.todo_filename, important_nums)
            content = "".join(todos)
            return content.strip("\n")