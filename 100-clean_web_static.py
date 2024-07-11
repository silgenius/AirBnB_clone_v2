#!/usr/bin/python3
"""
a Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean"""

import os
from fabric.api import *

env.hosts = ['54.88.64.221', '54.87.212.173']


def do_clean(number=0):
    """
    a Fabric script (based on the file 3-deploy_web_static.py) that deletes
    out-of-date archives, using the function do_clean:
    """  
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(archive)) for archive in archives]
    
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [archive for archive in archives if "web_static_" in archives]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(archive)) for archive in archives]
