FROM certbot/certbot

RUN mkdir -p /var/www/letsencrypt
RUN mkdir -p /nginx/
COPY  ["/Docker/certbot/docker-entrypoint.sh","/Docker/certbot/nginx.conf","/"]


#ENTRYPOINT [ "sh", "-c", "/bin/bash" ]
