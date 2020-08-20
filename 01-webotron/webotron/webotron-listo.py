#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Webtron: Deploy website with AWS
Webtron automates the process of deploying static web
- Configure AWS s3 buckets
    - Create them
    - Set them up fpr static website hosting
    - Deploy local code to them
- Configure DNS with route53
- Configure content delivery network and SSL
"""

import boto3
import click
from botocore.exceptions import ClientError
from pathlib import Path

session = boto3.Session(profile_name='default')
s3 = session.resource('s3')

@click.group()
def cli():
    """Webtron deploys website to AWS"""
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_buckets_objects(bucket):
    """List objects in s3 bucket"""
    for obj in  s3.Bucket(bucket).objects.all():
        print(obj)





if __name__ == "__main__":  
    cli()