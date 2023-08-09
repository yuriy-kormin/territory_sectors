FROM node:alpine

COPY ["frontend/package.json","Docker/react/docker-entrypoint.sh","/"]
WORKDIR /
RUN npm install --omit-dev --package-lock-only &&\
    npm ci --global-style &&  \
    npm cache clean --force
CMD ["/docker-entrypoint.sh"]