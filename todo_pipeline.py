#!/usr/bin/python
# !-*- coding:utf-8 -*-

import pipeline
import todo_handler


class TodoPipeline(pipeline.Pipeline):

    def __init__(self):
        super().__init__()
        self.add_handler(todo_handler.TodoHandler())
