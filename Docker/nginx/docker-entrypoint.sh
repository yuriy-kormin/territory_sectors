#!/bin/bash
set -e

if [ -f /etc/nginx/conf.d/default.conf ]; then
    rm /etc/nginx/conf.d/default.conf
fi

#making log dir with files
nginx_log_dir="/var/log/nginx"
access_log_file="access.log"
error_log_file="error.log"

# Check if the directory exists
if [ ! -d "$nginx_log_dir" ]; then
  # Create the directory
  sudo mkdir -p "$nginx_log_dir"
  echo "Created directory $nginx_log_dir"
  # Create access log file with root:root ownership
  sudo touch "$nginx_log_dir/$access_log_file"
  sudo chown root:root "$nginx_log_dir/$access_log_file"
  echo "Created $access_log_file with root:root ownership"

  # Create error log file with root:root ownership
  sudo touch "$nginx_log_dir/$error_log_file"
  sudo chown root:root "$nginx_log_dir/$error_log_file"
  echo "Created $error_log_file with root:root ownership"
else
  echo "Directory $nginx_log_dir already exists"
fi

### copy config files if necessary
NGINX_TEMPLATE_DIR="/etc/nginx/conf.templates/"
NGINX_CONF_DIR="/etc/nginx/conf.d/"

if [ -f "${NGINX_CONF_DIR}nginx-ssl.conf" ]; then
  echo "ssl config exists. skip configuration"
else
  echo "ssl config file not found. start configuration"

  rm -f "${NGINX_CONF_DIR}/*"
  echo "removing all files from ${NGINX_CONF_DIR}"

  cp "${NGINX_TEMPLATE_DIR}"/* "${NGINX_CONF_DIR}"
  echo "copy config from templates"

fi
##start daemon
service nginx start

function run_command {
  echo "Config file changed! Reloading nginx..."
  service nginx reload
}

# Use inotifywait to monitor the directory for changes
inotifywait -m /etc/nginx/conf.d/ -e move |
    run_command