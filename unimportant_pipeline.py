#!/usr/bin/python
# !-*- coding:utf-8 -*-

import pipeline
import unimportant_handler
import todo_handler


class UnimportantPipeline(pipeline.Pipeline):
    def __init__(self):
        super().__init__()
        self.add_handler(unimportant_handler.UnimportantHandler())
        self.add_handler(todo_handler.TodoHandler())
