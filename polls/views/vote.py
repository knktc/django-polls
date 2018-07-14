#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vote pages

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 17:18
"""

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


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
    return render_to_response('index.html', context={})
