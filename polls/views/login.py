#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 17:18
"""

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

__author__ = 'knktc'
__version__ = '0.1'


def login_page(request):
    """
    show login page
    :param :
    :return:
    :rtype:
    """
    return render_to_response('login.html')


@csrf_exempt
def login_action(request):
    """
    log the user in
    :param :
    :return:
    :rtype:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render_to_response('login.html', context={'login_failed': True})
