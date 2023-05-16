#!/usr/bin/python3
"""This is a Fabric script that distributes an archive to our 
web servers, using the function do_deploy: 
"""

from fabric.api import *
from datetime import datetime
from os.path import exists


# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
env.hosts = ['ubuntu@35.174.204.79', 'ubuntu@34.227.91.64']
#env.users = 'ubuntu'



def do_deploy(archive_path):
    """ This function distributes an archive to our web servers
    """
    if exists(archive_path) is False:
        return False  # Returns False if the file at archive_path doesnt exist
    filename = archive_path.split('/')[-1]
    # change filename, let it be without .tgz
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    # curr = '/data/web_static/current'
    tmp = "/tmp/" + filename

    try:
        #Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Uncompress the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        #Delete the archive from the web server
        run("rm -rf /data/web_static/current")
        #Delete the symbolic link /data/web_static/current from the web server
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        return True
    except:
        return False
