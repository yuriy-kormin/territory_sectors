FROM node:alpine as build
#ARG REACT_APP_BACKEND_URL="http://localhost/graphql/"
#ARG CERTBOT_DOMAINS="localhost"

#RUN DOMAIN=$(echo $CERTBOT_DOMAINS | cut -d',' -f1)
#ENV REACT_APP_BACKEND_URL "$REACT_APP_BACKEND_URL:"http://$DOMAIN/graphql/""
#ARG CERTBOT_DOMAINS
#ENV CERTBOT_DOMAINS=$CERTBOT_DOMAINS

WORKDIR /app/
COPY ["frontend/", "/Docker/nginx/docker-setenv.sh" , "./"]
# RUN DOMAIN=$(echo $CERTBOT_DOMAINS | cut -d',' -f1) && \
#    REACT_APP_BACKEND_URL="http://${DOMAIN}/graphql/" && \
#    echo "Setting REACT_APP_BACKEND_URL to $REACT_APP_BACKEND_URL" && \
#    export REACT_APP_BACKEND_URL

RUN echo $REACT_APP_BACKEND_URL

# RUN chmod +x docker-setenv.sh && \
#    ./docker-setenv.sh  && \
RUN npm install --omit=dev && \
    npm run build

#chmod +x docker-setenv.sh && \
#    ./docker-setenv.sh  && \


FROM nginx

RUN apt-get update && \
    apt-get install -y inotify-tools sudo &&\
    mkdir -p /etc/nginx/conf.templates &&\
    rm -rf /usr/share/nginx/html/*
COPY ["/Docker/nginx/nginx.conf","/Docker/nginx/nginx-ssl.tmp","/etc/nginx/conf.templates/"]

COPY --from=build /app/build /usr/share/nginx/html

COPY /Docker/nginx/docker-entrypoint.sh /
