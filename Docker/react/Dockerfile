FROM node:alpine

COPY ["frontend/package.json","frontend/package-lock.json","Docker/react/docker-entrypoint.sh","/"]
WORKDIR /
RUN npm install -g npm@latest &&\
    npm ci --install-strategy=shallow --omit=dev &&  \
    npm cache clean --force
CMD ["/docker-entrypoint.sh"]