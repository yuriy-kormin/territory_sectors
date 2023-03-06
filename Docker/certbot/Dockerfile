FROM certbot/certbot

RUN mkdir -p /var/www/letsencrypt
RUN mkdir -p /nginx/
COPY /Docker/certbot/docker-entrypoint.sh /
ENTRYPOINT [ "sh", "-c", "docker-entrypoint.sh" ]
