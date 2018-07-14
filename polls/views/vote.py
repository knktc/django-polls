#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vote pages

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 17:18
"""

from django.http import Http404, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from polls.models import Question, Choice, VoteRecord
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.utils import timezone


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

    return render(request, 'index.html', {'questions': questions})


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
    except ObjectDoesNotExist:
        raise Http404('question id does not exist')

    # get choices
    choices = Choice.objects.filter(question=question_obj)
    return render(request, 'vote_page.html', {'question': question_obj, 'choices': choices})


@login_required
def vote_action(request, **kwargs):
    """
    vote action
    :param :
    :return:
    :rtype:
    """
    question_id = kwargs.get('id')
    vote_choice = request.POST.get('choice')
    user_obj = request.user

    # get question
    try:
        question_obj = Question.objects.get(id=question_id)
    except ObjectDoesNotExist:
        raise Http404('question id does not exist')

    # check vote record
    record = VoteRecord.objects.filter(question=question_obj, user=user_obj).order_by('-vote_time')[0]
    if record and (timezone.now() - record.vote_time).seconds < settings.VOTE_INTERVAL:
        return HttpResponseForbidden('vote limit exceeded')

    # check choice
    try:
        vote_choice = int(vote_choice)
    except ValueError:
        return HttpResponseBadRequest('malformed choice id')

    choice_obj = Choice.objects.filter(question=question_obj, id=vote_choice)[0]
    if not choice_obj:
        raise Http404('choice id and question do not match')

    # write vote record
    record = VoteRecord(question=question_obj, user=user_obj, choice=choice_obj)
    record.save()

    return redirect('/')


@login_required
def vote_result_page(request):
    """
    show vote stat
    :param :
    :return:
    :rtype:
    """
    pass
