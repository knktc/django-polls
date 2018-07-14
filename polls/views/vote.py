#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vote pages

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 17:18
"""

from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from polls.models import Question, Choice
from django.core.exceptions import ObjectDoesNotExist


__author__ = 'knktc'
__version__ = '0.1'


@login_required
def polls_page(request):
    """
    show polls list
    :param :
    :return:
    :rtype:
    """
    questions = Question.objects.filter(enable=True).order_by('-update_time')

    return render_to_response('index.html', context={'questions': questions})


@login_required
def vote_page(request, **kwargs):
    """
    show vote page
    :param :
    :return:
    :rtype:
    """
    question_id = kwargs.get('id')
    try:
        # get question
        question_obj = Question.objects.get(id=question_id)

        # get choices
        choices = Choice.objects.filter(question=question_obj)
    except ObjectDoesNotExist:
        raise Http404

    return render_to_response('vote_page.html', context={'question': question_obj, 'choices': choices})


@login_required
def vote_action(request):
    """
    vote action
    :param :
    :return:
    :rtype:
    """
    pass

