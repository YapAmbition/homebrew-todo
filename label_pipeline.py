#!/usr/bin/python
# !-*- coding:utf-8 -*-


import pipeline
import label_handler
import todo_handler


class LabelPipeline(pipeline.Pipeline):

    def __init__(self):
        super().__init__()
        self.add_handler(label_handler.LabelHandler())
        self.add_handler(todo_handler.TodoHandler())
