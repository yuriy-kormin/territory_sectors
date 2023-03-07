#!/bin/bash
set -e

if [ -f /etc/nginx/conf.d/default.conf ]; then
    rm /etc/nginx/conf.d/default.conf
fi
cp /app/nginx.conf /etc/nginx/conf.d/nginx.conf

#envsubstr </app/nginx-ssl.tmp >/etc/nginx/conf.d/nginx-ssl.tmp
sed -i "s/\$CERTBOT_DOMAINS/$CERTBOT_DOMAINS/g" /app/nginx-ssl.tmp
cp /app/nginx-ssl.tmp /etc/nginx/conf.d/nginx-ssl.tmp

nginx -g "daemon off;"
