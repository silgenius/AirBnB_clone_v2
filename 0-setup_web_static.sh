#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# check if nginx is installed
if ! command -v nginx &> /dev/null
then
        sudo apt-get update
        sudo apt install nginx -y
        sudo service nginx start
fi

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html

printf %s "<html>
  <head>
  </head>
  <body>
    Alx School
  </body>
</html>
" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R "$USER":"$USER" /data
sudo chown -R "$USER":"$USER" /etc/nginx/

content="server_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\
        \n\t\tindex index.html index.htm;\n\t}\n"
sudo sed -i "s|server_name _;|${content}|g" /etc/nginx/sites-available/default

sudo service nginx restart
