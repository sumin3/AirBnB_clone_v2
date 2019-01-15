#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
if [ ! -x /usr/sbin/nginx ]
then
    apt-get -y update
    apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "Holberton School!" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
file="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static {" $file
then
    sed -i '/^\tserver_name localhost;/ a\\n\tlocation \/hbnb_static \{\n\t\talias /data/web_static/current/;\n\t\}\n' $file
    service nginx restart
fi
