#!/usr/bin/python3
"""
 a Fabric script (based on the file 1-pack_web_static.py) that distributes
 an archive to your web servers, using the function do_deploy:
 """

from fabric.api import env, put, run
import os

env.hosts = ['54.88.64.221', '54.87.212.173']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False
    
    try:
        # Extract the archive file name and its base name without extension
        archive_file = os.path.basename(archive_path)
        archive_no_ext = archive_file.split('.')[0]
        
        # Define target paths
        tmp_path = f'/tmp/{archive_file}'
        release_path = f'/data/web_static/releases/{archive_no_ext}/'

        # Upload the archive to the /tmp/ directory
        put(archive_path, tmp_path)

        # Create the release directory
        run(f'mkdir -p {release_path}')

        # Uncompress the archive
        run(f'tar -xzf {tmp_path} -C {release_path}')

        # Move the contents out of the extracted folder
        run(f'mv {release_path}web_static/* {release_path}')
        run(f'rm -rf {release_path}web_static')

        # Delete the archive from the web server
        run(f'rm {tmp_path}')

        # Delete the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run(f'ln -s {release_path} /data/web_static/current')

        return True

    except Exception as e:
        return False
