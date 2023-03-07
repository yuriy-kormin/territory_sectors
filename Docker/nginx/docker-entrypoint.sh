#!/bin/bash
set -e

if [ -f /etc/nginx/conf.d/default.conf ]; then
    rm /etc/nginx/conf.d/default.conf
fi
cp /app/nginx.conf /etc/nginx/conf.d/nginx.conf

#envsubstr </app/nginx-ssl.tmp >/etc/nginx/conf.d/nginx-ssl.tmp
sed -i "s/\$CERTBOT_DOMAINS/$CERTBOT_DOMAINS/g" /app/nginx-ssl.tmp
cp /app/nginx-ssl.tmp /etc/nginx/conf.d/nginx-ssl.tmp

# Define a function to run the command you want to run when the file changes
function run_command {
  # Replace this with the command you want to run
  echo "Config file changed! Reloading nginx..."
  nginx -s reload
}

# Use inotifywait to monitor the directory for changes
inotifywait -m /etc/nginx/conf.d/ -e modify |
  while read path action file; do
    if [[ "$file" == *.conf ]]; then
      run_command
    fi
  done

#CMD ["sh", "-c", "while inotifywait -e modify,create,delete /etc/nginx/conf.d/; do nginx -s reload; done & nginx -g \"daemon off;\""]
nginx -g "daemon off;"
