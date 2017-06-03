from django.apps import AppConfig
import os
import sys

class PollsConfig(AppConfig):
    name = 'polls'
os.environ['DJANGO_SETTNGS_MODULE']='setings'
sys.path.append(r'')
