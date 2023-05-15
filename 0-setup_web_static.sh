#!/usr/bin/env bash
#This script sets up web servers for the deployment of web_static


# Check if Nginx is not installed and install it
if ! dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -q "ok installed"; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared /data/web_static/releases

# Create a fake HTML file for testing
sudo echo "Hello World! \n Fake HTML file" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
