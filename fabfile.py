#!/usr/bin/python3
""" This module contains the function do_pack that generates a .tgz archive
  from the contents of the web_static folder (fabric script) """


from fabric.api import *
from datetime import datetime


def do_pack():
    """ This function generates a .tgz archive from the contents of the
    web_static folder """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    archive_result = local("sudo tar -cvzf {} web_static".format(file_name))
    if archive_result.succeeded:
        return file_name
    else:
        return None