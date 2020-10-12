#!/usr/bin/python
# !-*- coding:utf-8 -*-

import pipeline
import important_handler
import todo_handler
import red_font_handler


class ImportantPipeline(pipeline.Pipeline):
    def __init__(self):
        super().__init__()
        self.add_handler(important_handler.ImportantHandler())
        self.add_handler(todo_handler.TodoHandler())
        self.add_handler(red_font_handler.RedFontHandler())
