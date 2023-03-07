FROM nginx:latest

ARG CERTBOT_DOMAINS=test2.nitochka.site
#ENV CERTBOT_DOMAINS=$CERTBOT_DOMAINS

RUN rm /etc/nginx/conf.d/default.conf
COPY ["/Docker/nginx/nginx.conf","/Docker/nginx/nginx-ssl.tmp", "/etc/nginx/conf.d/"]
RUN sed -i "s/\$CERTBOT_DOMAINS/$CERTBOT_DOMAINS/g" /etc/nginx/conf.d/default.conf