#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# check if nginx is installed
check=$(which nginx)
if [ -z $check ]; then
	sudo apt-get update
	sudo apt install nginx -y
	sudo service nginx start
fi

mkdir /data
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
</html>" >> /data/web_static/releases/test/index.html

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data

printf %s "server {
	listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

	location /hbnb_static {
		alias /data/web_static/current/
	}
}" >> /etc/nginx/sites-available/default

sudo service nginx restart
