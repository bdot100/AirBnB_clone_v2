#!/usr/bin/python3
"""This script distributes and archive
 to our web servers"""

import os.path
from fabric.api import *

env.hosts = ["35.174.204.79", "34.227.91.64"]


def do_deploy(archive_path):
    """This Function distributes an archive
    file to our web servers"""

    if not os.path.exists(archive_path):
        return False
    try:
        tgz_file = archive_path.split("/")[-1]
        print(tgz_file)
        file_name = tgz_file.split(".")[0]
        print(file_name)
        path_name = "/data/web_static/releases/" + file_name
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("tar -zxvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgz_file, file_name))
        run("rm /tmp/{}".format(tgz_file))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name))
        return True
    except Exception as e:
        return False
