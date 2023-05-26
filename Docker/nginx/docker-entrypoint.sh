#!/bin/bash
set -e

if [ -f /etc/nginx/conf.d/default.conf ]; then
    rm /etc/nginx/conf.d/default.conf
fi
cp /app/nginx.conf /etc/nginx/conf.d/nginx.conf

#envsubstr </app/nginx-ssl.tmp >/etc/nginx/conf.d/nginx-ssl.tmp
sed -i "s/\$CERTBOT_DOMAINS/$CERTBOT_DOMAINS/g" /app/nginx-ssl.tmp
cp /app/nginx-ssl.tmp /etc/nginx/conf.d/nginx-ssl.tmp

#making log dir with files
nginx_log_dir="/var/log/nginx"
access_log_file="access.log"
error_log_file="error.log"

# Check if the directory exists
if [ ! -d "$nginx_log_dir" ]; then
  # Create the directory
  sudo mkdir -p "$nginx_log_dir"
  echo "Created directory $nginx_log_dir"
else
  echo "Directory $nginx_log_dir already exists"
fi

# Create access log file with root:root ownership
sudo touch "$nginx_log_dir/$access_log_file"
sudo chown root:root "$nginx_log_dir/$access_log_file"
echo "Created $access_log_file with root:root ownership"

# Create error log file with root:root ownership
sudo touch "$nginx_log_dir/$error_log_file"
sudo chown root:root "$nginx_log_dir/$error_log_file"
echo "Created $error_log_file with root:root ownership"

# Define a function to run the command you want to run when the file changes
function run_command {
  # Replace this with the command you want to run
  echo "Config file changed! Reloading nginx..."
  service nginx reload
}

# Use inotifywait to monitor the directory for changes
inotifywait -m /etc/nginx/conf.d/ -e move |
    run_command
  done &

#CMD ["sh", "-c", "while inotifywait -e modify,create,delete /etc/nginx/conf.d/; do nginx -s reload; done & nginx -g \"daemon off;\""]
nginx -g "daemon off;"
