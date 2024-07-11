#!/usr/bin/env python3

"""
 a Fabric script (based on the file 1-pack_web_static.py) that distributes
 an archive to your web servers, using the function do_deploy
"""

from fabric.api import sudo, put, env
import os


env.hosts = ['54.88.64.221', '54.87.212.173']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name = filename.split('.')[0]
    try:
        put(archive_path, '/tmp/')
        sudo(f'mkdir -p /data/web_static/releases/{name}')
        sudo(f'tar -xzf /tmp/{filename} -C /data/web_static/releases/{name}')
        sudo(f'rm /tmp/{filename}')
        sudo(f'mv /data/web_static/releases/{name}/web_static/*  /data/web_static/releases/{name}')
        sudo('rm /data/web_static/current')
        sudo(f'ln -s /data/web_static/releases/{name} /data/web_static/current')
    except Exception as e:
        return False

    return True
