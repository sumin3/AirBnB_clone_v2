#!/usr/bin/python3
# Fabric script that generates a .tgz archive from
# the contents of the web_static folder
# of your AirBnB Clone repo, using the function do_pack.
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    local("mkdir -p versions", capture=False)
    created_time = datetime.now()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(created_time.year,
                                                     created_time.month,
                                                     created_time.day,
                                                     created_time.hour,
                                                     created_time.minute,
                                                     created_time.second)
    arch_path = "versions/" + file_name
    source_dir = "web_static"
    try:
        file_path = local("tar -cvzf {} {}".format(arch_path, source_dir),
                          capture=False)
        file_size = os.stat(arch_path).st_size
        full_arch_path = os.getcwd() + "/versions"
        print("web_static packed: {} -> {}Bytes".format(arch_path, file_size))
        return full_arch_path
    except:
        return None
