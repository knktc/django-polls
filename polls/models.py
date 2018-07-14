#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 16:38
"""

from django.contrib.auth.models import User
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
    question_text = models.CharField(unique=True, max_length=256, verbose_name='question')

    def __str__(self):
        return self.question_text


class Choice(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    enable = None

    def __str__(self):
        return self.choice_text

    class Meta:
        unique_together = ('question', 'choice_text',)


class VoteRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    vote_time = models.DateTimeField(auto_now_add=True)
