#!/usr/bin/python3

"""
 a Fabric script (based on the file 1-pack_web_static.py) that distributes
 an archive to your web servers, using the function do_deploy
"""

from fabric.api import sudo, put, env
import os

env.user = 'ubuntu'env.user = 'ubuntu'
env.hosts = ['54.88.64.221', '54.87.212.173']
env.key_filename = "~/.ssh/id_rsa_alx"


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """

    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name = filename.split('.')[0]

    result = put(archive_path, '/tmp/')
    if result.failed:
        return False
    result = sudo(f'mkdir -p /data/web_static/releases/{name}')
    if result.failed:
        return False
    result = sudo(f'tar -xzf /tmp/{filename} -C /data/web_static/releases/{name}')
    if result.failed:
        return False
    result = sudo(f'rm /tmp/{filename}')
    if result.failed:
        return False
    result = sudo(f'mv /data/web_static/releases/{name}/web_static/* /data/web_static/releases/{name}')
    if result.failed:
        return False
    result = sudo('rm -rf /data/web_static/current')
    if result.failed:
        return False
    result = sudo (f'rm -rf /data/web_static/releases/{name}/web_static')
    if result.failed:
        return False
    result = sudo(f'ln -s /data/web_static/releases/{name} /data/web_static/current')
    if result.failed:
        return False

    return True
