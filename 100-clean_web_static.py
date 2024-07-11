#!/usr/bin/python3
"""
a Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean"""

import os
from fabric.api import *


env.hosts = ['54.88.64.221', '54.87.212.173']
env.user = 'ubuntu'

def do_clean(number=0):
    """
    a Fabric script (based on the file 3-deploy_web_static.py) that deletes
    out-of-date archives, using the function do_clean:
    """  
    if number < 1:
        number = 1

    # Clean local versions folder
    with lcd("versions"):
        local_archives = local("ls -1t", capture=True).split()
        archives_to_delete = local_archives[number:]
        for archive in archives_to_delete:
            local("rm ./{}".format(archive))

    # Clean remote releases folder
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -1t").split()
        archives_to_delete = remote_archives[number:]
        for archive in archives_to_delete:
            run("rm -rf ./{}".format(archive))
