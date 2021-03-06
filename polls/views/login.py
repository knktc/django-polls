#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 17:18
"""

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

__author__ = 'knktc'
__version__ = '0.1'


def login_page(request):
    """
    show login page
    :param :
    :return:
    :rtype:
    """
    return render(request, 'login.html')


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
        return render(request, 'login.html', {'login_failed': True})


def logout_action(request):
    """
    log out
    :param :
    :return:
    :rtype:
    """
    logout(request)
    return redirect('/login_page/')

