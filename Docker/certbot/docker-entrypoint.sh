#!/bin/bash

certbot certonly --agree-tos --keep-until-expiring --webroot -w /var/www/letsencrypt --no-eff-email --email "${CERTBOT_EMAIL}" -d "${CERTBOT_DOMAINS}"
envsubstr </nginx.conf >/nginx/nginx-ssl.conf
