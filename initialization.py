#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a initialization scripts

"""
@author:knktc
@contact:me@knktc.com
@create:2018-07-14 23:41
"""

import os
import sys

import django

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(SCRIPT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'polls.settings'
django.setup()

from django.contrib.auth.models import User
from polls.models import Question
from django.core.management import call_command


__author__ = 'knktc'
__version__ = '0.1'

# config
SUPERUSER_USERNAME = 'admin'
SUPERUSER_PASSWORD = 'adminadmin'
SUPERUSER_EMAIL = 'me@knktc.com'

NORMAL_USERS = [
    {'username': 'user1', 'password': 'password'},
    {'username': 'user2', 'password': 'password'},
    {'username': 'user3', 'password': 'password'},
]

PRESET_DATA = [
    {
        'question': 'What is the best video game of all time?',
        'choices': [
            'Overwatch',
            'World of Warcraft',
            'PUBG',
            'League of Legends',
        ]
    }
]


def main():
    """
    main process

    """
    # check db
    db_filepath = os.path.join(SCRIPT_DIR, 'db.sqlite3')
    if os.path.isfile(db_filepath):
        flag = input('db.sqlite3 file exists, remove(y) or abort(n):')
        if flag == 'y':
            os.remove(db_filepath)
        else:
            print('aborting...')
            sys.exit(1)

    # generate db
    call_command("migrate", interactive=True)

    # add default superuser
    user_obj = User.objects.create_superuser(username=SUPERUSER_USERNAME,
                                             password=SUPERUSER_PASSWORD,
                                             email=SUPERUSER_EMAIL)
    user_obj.save()

    print('superuser created')

    # add other users
    for single_user in NORMAL_USERS:
        user_obj = User.objects.create_user(username=single_user.get('username'), password=single_user.get('password'))
        user_obj.save()

    print('normal users imported')

    # write the preset data
    for single_data in PRESET_DATA:
        question_obj = Question(question_text=single_data.get('question'))
        question_obj.save()
        for choice in single_data.get('choices'):
            question_obj.choice_set.create(choice_text=choice)
            question_obj.save()
    print('preset data imported')

    print('done!')


if __name__ == '__main__':
    main()
