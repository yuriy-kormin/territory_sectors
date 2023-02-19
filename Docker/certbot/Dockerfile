FROM certbot/certbot

RUN mkdir -p /var/www/letsencrypt

ENTRYPOINT [ "sh", "-c", "certbot certonly --agree-tos --webroot --webroot-path /var/www/letsencrypt --no-eff-email --email $CERTBOT_EMAIL -d $CERTBOT_DOMAINS" ]
