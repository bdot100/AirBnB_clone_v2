#!/usr/bin/python3
"""
This script distributes an archive to the web servers, using the do_deploy function.
"""
from fabric.api import env, put, run, sudo, cd
import os


env.hosts = ['ubuntu@35.174.204.79', 'ubuntu@34.227.91.64']
env.user = 'ubuntu'
env.key_filename = 'school'


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    # Get the name of the archive
    file_name = os.path.basename(archive_path)
    name_only = os.path.splitext(file_name)[0]

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    run("sudo mkdir -p /data/web_static/releases/{}".format(name_only))
    run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, name_only))

    # Delete the archive from the web server
    run("sudo rm /tmp/{}".format(file_name))

    # Move the files to the appropriate directory
    run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name_only, name_only))

    # Remove the old directory
    run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name_only))

    # Delete the symbolic link /data/web_static/current from the web server
    sudo("sudo rm -rf /data/web_static/current")

    # Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
    sudo("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name_only))

    return True
