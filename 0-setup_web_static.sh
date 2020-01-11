#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
if [ ! -d /data/web_static/releases/test ]; then
    sudo mkdir -p /data/web_static/releases/test/;
fi;
if [ ! -d /data/web_static/shared ]; then
    sudo mkdir -p /data/web_Static/shared/;
fi;
sudo chown -R ubuntu. /etc/nginx/sites-available
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sfn /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu. /data
sudo sed -i '35ilocation /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
