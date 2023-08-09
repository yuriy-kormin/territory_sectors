FROM node:alpine

COPY ["frontend/package.json","Docker/react/docker-entrypoint.sh","/"]
WORKDIR /
RUN npm install --omit-dev -g -f  &&\
    npm ci &&  \
    npm cache clean --force
CMD ["/docker-entrypoint.sh"]