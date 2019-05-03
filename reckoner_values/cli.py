#!/usr/bin/python3
from .git_values import GitValues
from .meta import __version__
from .reckoner_file_updater import ReckonerFileUpdater
from .s3_values import S3Values
from pathlib import Path
import click
import coloredlogs
import json
import os

@click.command()
@click.option('--namespace', default="default", help='The namespace for the release')
@click.option('--chart', default="nginx", help='The name of the chart')
@click.option('--app', required="true", help='The app name for the release')
@click.option('--extrafiles', help='Extra file names to search for')
@click.option('--extravalues', help='Full paths to extra values files')
@click.option('--destination', default="/tmp", help='The destination for downloaded values files')
@click.option('--bucket', required="true", help='The source s3 bucket name')
@click.option('--output', required="true", default='json', help='The source s3 bucket name', type=click.Choice(['json', 'helm']))
@click.option('--region', default=False, help='The target region')
def cli(namespace, chart, app, extrafiles, extravalues, destination, bucket, output, region):
    """Build all possible s3 paths for values files"""
    if extrafiles == None:
        extrafiles = []
    else:
        extrafiles = extrafiles.split(',')
    if extravalues == None:
        extravalues = []
    else:
        extravalues = extravalues.split(',')
    if bucket == "git":
        bp = GitValues(namespace, chart, app, region, extrafiles, extravalues)
    else:
        bp = S3Values(namespace, chart, app, region, extrafiles, extravalues)
    downloaded = bp.download_values(bucket, destination)
    if output == 'json':
        print(json.dumps(downloaded))
    elif output == 'helm':
        helm_args = ''
        for file in downloaded:
            helm_args = helm_args + ' --values ' + file
        print(helm_args)

@click.command()
def version():
    """ Takes no arguments, outputs version info"""
    print(__version__)

@click.command()
@click.option('--source', required=True, help='The source autohelm file')
@click.option('--dest', required=True, help='The destination autohelm file')
@click.option('--region', required=True, help='The target region')
@click.option('--values', required=True, help='Path to the values files')
def update_reckoner_file(source, dest, region, values):
    rfu = ReckonerFileUpdater(source=source, dest=dest, region=region, download_path=values)
    rfu.update()