FROM node:alpine

COPY ["frontend/package.json","Docker/react/docker-entrypoint.sh","/"]
WORKDIR /
RUN npm install --omit-dev -g -f --package-lock-only &&\
    npm ci &&  \
    npm cache clean --force
CMD ["/docker-entrypoint.sh"]