#!/usr/bin/env python
# -*- coding: utf-8 -*-
# custom admin page

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 16:57
"""

from django.contrib import admin

from polls.models import Question, Choice

__author__ = 'knktc'
__version__ = '0.1'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)
    fields = ('question_text', 'enable')
    list_display = ('question_text', 'enable', 'create_time', 'update_time')
    ordering = ('-update_time', )
