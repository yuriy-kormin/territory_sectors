#!/bin/bash

sed -i "s/\$CERTBOT_DOMAINS/$CERTBOT_DOMAINS/g" /etc/nginx/conf.d/nginx.conf
