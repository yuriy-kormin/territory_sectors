FROM node:alpine

COPY ["frontend/package.json","Docker/react/docker-entrypoint.sh","/"]
WORKDIR /
RUN npm install -g npm@latest &&\
    npm install --omit-dev --package-lock-only &&\
    npm ci --global-style  --omit=dev &&  \
    npm cache clean --force
CMD ["/docker-entrypoint.sh"]