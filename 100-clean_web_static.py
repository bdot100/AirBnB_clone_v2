#!/usr/bin/python3
# This Fab script deletes out-of-date archives.
import os
from fabric.api import *

# Declear env.hosts
env.hosts = ['ubuntu@35.174.204.79', 'ubuntu@34.227.91.64']


def do_clean(number=0):
    """This is used to delete out-of-date archives
    Args:
        number (int): The number of archives to keep.

    Instruction: If number is equal 0 or 1, keeps only
    the most recent archive. If number is 2, keep the
    most and second-most recent archives etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
