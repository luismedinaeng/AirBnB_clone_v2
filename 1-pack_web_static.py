#!/usr/bin/python3
'''
Module that generates tgz file with the content of web_server directories
'''
import datetime
from fabric.api import *


def do_pack():
    local("mkdir -p versions")
    current = datetime.datetime.now()
    file_tgz = "web_static_{}.tgz".format(current.strftime("%Y%m%d%H%M%S"))
    if local("tar -cvzf versions/{} web_static".format(file_tgz)).failed:
        return None
    else:
        return file_tgz
