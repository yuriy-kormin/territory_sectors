FROM certbot/certbot

RUN mkdir -p /var/www/letsencrypt
RUN mkdir -p /nginx/
COPY  ["/Docker/certbot/docker-entrypoint.sh","/Docker/certbot/nginx.conf","/"]


#ENTRYPOINT [ "sh", "-c", "certbot certonly --agree-tos --keep --webroot --webroot-path /var/www/letsencrypt --no-eff-email --email $CERTBOT_EMAIL -d $CERTBOT_DOMAINS" ]
