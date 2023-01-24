FROM postgis/postgis:latest

RUN mkdir /docker-entrypoint-initdb.d
COPY Docker/postgis/init.sql /docker-entrypoint-initdb.d/

