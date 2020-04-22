#!/usr/bin/python3
'''
Module that generates tgz file with the content of web_server directories
'''
import datetime
from fabric.api import *

env.hosts = ['34.74.55.34', '3.82.65.220']


def do_pack():
    local("mkdir -p versions")
    current = datetime.datetime.now()
    file_tgz = "web_static_{}.tgz".format(current.strftime("%Y%m%d%H%M%S"))
    if local("tar -cvzf versions/{} web_static".format(file_tgz)).failed:
        return None
    else:
        return file_tgz

def do_deploy(archive_path):
    if local("ls {}".format(archive_path)).failed:
        return False
    archive_name = archive_path.split('/')[-1]
    folder = archive_name.split('.')[0]
    if put(archive_path, "/tmp/{}".format(archive_name)).failed:
        return False
    run("mkdir -p /data/web_static/releases/{}".format(folder))
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
           format(archive_name, folder)).failed:
        return False
    run("rm /tmp/{}".format(archive_name))
    run("mv /data/web_static/releases/{0}/web_static/* /data/web_static/releases/{0}/"
        .format(folder))
    run("rm -rf /data/web_static/realeases/{}/web_static".format(folder))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(folder))
    return True
