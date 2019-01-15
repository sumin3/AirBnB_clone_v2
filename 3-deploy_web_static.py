#!/usr/bin/python3
# Write a Fabric script (based on the file 1-pack_web_static.py)
# that distributes an archive to your web server
from datetime import datetime
from fabric.api import local, put, env, run
import os
env.hosts = ['35.185.103.245', '35.243.154.87']
env.user = "ubuntu"


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
        print("web_static packed: {} -> {}Bytes".format(arch_path, file_size))
        return arch_path
    except:
        return None


def do_deploy(archive_path):
    if os.path.isfile(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        arch_filename_tgz = archive_path.split('/')[1]
        arch_filename_no_tgz = arch_filename_tgz.split('.')[0]
        target_path = "/data/web_static/releases/{}/".format(
            arch_filename_no_tgz)
        run("sudo mkdir -p {}".format(target_path))
        run("sudo tar -xzf /tmp/{} -C {}"
            .format(arch_filename_tgz, target_path))
        run("sudo rm /tmp/{}".format(arch_filename_tgz))
        run("sudo mv {}web_static/* {}".format(target_path, target_path))
        run("sudo rm -rf {}web_static".format(target_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target_path))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    try:
        created_archive = do_pack()
        do_deploys = do_deploy(created_archive)
        return do_deploys
    except:
        return False
