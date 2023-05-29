FROM nginx:latest

RUN apt-get update && apt-get install -y inotify-tools sudo
RUN mkdir -p /etc/nginx/conf.templates
COPY ["/Docker/nginx/nginx.conf","/Docker/nginx/nginx-ssl.tmp","/etc/nginx/conf.templates/"]
COPY /Docker/nginx/docker-entrypoint.sh /
