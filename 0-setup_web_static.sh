#!/usr/bin/env bash
# Script that install nginx and setup the server to
# serve the content of /data/web_static/current to hbnb_static
apt-get install nginx --assume-yes
mkdir --parents /data/web_static/releases/test
mkdir --parents /data/web_static/shared
echo "Hello World! This is a test file" >> /data/web_static/releases/test/index.html
ln --force --symbolic /data/web_static/releases/test /data/web_static/current
chown --recursive ubuntu:ubuntu /data
OLD="server_name _;"
NEW="server_name _;\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"
sed -i "s/$OLD/$NEW/g" /etc/nginx/sites-available/default
service nginx restart
