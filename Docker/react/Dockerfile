FROM node:alpine

COPY ["frontend/package.json","Docker/react/docker-entrypoint.sh","/"]

RUN npm install --production -g -f --save &&\
    npm ci &&  \
    npm cache clean --force
CMD ["/docker-entrypoint.sh"]