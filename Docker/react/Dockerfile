

COPY ["frontend/package-lock.json","/npm/"]
COPY Docker/react/docker-entrypoint.sh /
WORKDIR /npm/

npm install --omit=dev --global

CMD ["/docker-entrypoint.sh"]