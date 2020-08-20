# coding: utf-8
import boto3
session = boto3.Session(profile_name='default')
s3 = session.resource('s3')

get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession.py 1-10')
