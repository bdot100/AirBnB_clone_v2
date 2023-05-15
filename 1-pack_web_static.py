#!/usr/bin/python3
"""generates a .tgz archive from the contents
of the web_static folder"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a tgz archive from the contents of the web_static folder."""

    # Create the folder if it doesn't exist
    local('mkdir -p versions')

    # Generate the name of the archive
    time_format = "%Y%m%d%H%M%S"
    arc_name = "web_static_" + datetime.now().strftime(time_format) + ".tgz"

    # Create the path to the archive
    archive_path = "versions/" + arc_name

    # Create the archive
    local("tar -czvf {} web_static".format(archive_path))

    # Check if the archive was created
    if local("test -f {}".format(archive_path)).failed:
        return None

    return archive_path

