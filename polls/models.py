#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 16:38
"""

from django.db import models

__author__ = 'knktc'
__version__ = '0.1'


class BaseModel(models.Model):
    enable = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    question = models.TextField(verbose_name='question')


class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
