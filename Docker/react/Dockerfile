FROM node:alpine

COPY ["frontend/package.json","/npm/"]
COPY Docker/react/docker-entrypoint.sh /
WORKDIR /npm/

RUN npm install --omit=dev --global

CMD ["/docker-entrypoint.sh"]