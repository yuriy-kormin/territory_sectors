#!/bin/bash

rm /etc/nginx/conf.d/default.conf
cp /app/nginx.conf /etc/nginx/conf.d/nginx.conf

envsubstr </app/nginx-ssl.tmp >/nginx/conf.d/nginx-ssl.tmp
