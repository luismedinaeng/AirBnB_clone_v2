#!/usr/bin/env bash
# Script that install nginx and setup the server to
# serve the content of /data/web_static/current to hbnb_static
apt-get update --assume-yes
apt-get install nginx --assume-yes
mkdir --parents /data/web_static/releases/test
mkdir --parents /data/web_static/shared
echo "Hello World! This is a test file" > /data/web_static/releases/test/index.html
ln --force --symbolic /data/web_static/releases/test /data/web_static/current
chown --recursive ubuntu:ubuntu /data
OLD=$(grep --max-count=1 -e '^\s*server_name .*;$' /etc/nginx/sites-available/default)
NEW="$OLD""\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}"
sed -i "0,/$OLD/s//$NEW/" /etc/nginx/sites-available/default
rm /etc/nginx/sites-enabled/default
ln --symbolic /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
service nginx restart
