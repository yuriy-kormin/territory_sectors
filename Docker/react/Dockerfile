FROM node:alpine

COPY ["frontend/package.json","/npm/"]
COPY Docker/react/docker-entrypoint.sh /
WORKDIR /npm/

RUN npm install --production -g -f --save

CMD ["/docker-entrypoint.sh"]