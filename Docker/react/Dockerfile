FROM node:alpine

COPY ["frontend/package.json","frontend/package-lock.json","Docker/react/docker-entrypoint.sh","/"]
WORKDIR /
RUN npm install &&\
    npm ci --install-strategy=shallow --omit=dev --silent &&  \
    npm cache clean --force
CMD ["/docker-entrypoint.sh"]