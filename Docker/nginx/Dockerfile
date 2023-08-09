FROM node:alpine as build
ARG REACT_APP_BACKEND_URL="http://localhost/graphql/"
#RUN DOMAIN=$(echo $CERTBOT_DOMAINS | cut -d',' -f1)
#ENV REACT_APP_BACKEND_URL "$REACT_APP_BACKEND_URL:"http://$DOMAIN/graphql/""

WORKDIR /app/
COPY frontend/ .
RUN npm install --omit=dev && \
    npm run build

FROM nginx:latest

RUN apt-get update && apt-get install -y inotify-tools sudo
RUN mkdir -p /etc/nginx/conf.templates
COPY ["/Docker/nginx/nginx.conf","/Docker/nginx/nginx-ssl.tmp","/etc/nginx/conf.templates/"]

RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/build /usr/share/nginx/html

COPY /Docker/nginx/docker-entrypoint.sh /
