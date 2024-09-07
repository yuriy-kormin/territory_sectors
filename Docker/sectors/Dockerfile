FROM python:3.10

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal

COPY ["pyproject.toml","README.md","poetry.lock","/poetry/"]
COPY Docker/sectors/docker-entrypoint.sh /
COPY --chmod=644 Docker/sectors/cronjob /etc/cron.d/cronjob

WORKDIR /poetry

RUN apt-get update && apt-get install -y  \
    binutils \
    libproj-dev \
    gdal-bin \
    libpq-dev \
    libgdal-dev \
    cron\
    --upgrade && \
    python3 -m pip install --upgrade pip &&\
    pip3 install  \
    whitenoise \
    gunicorn \
    poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root && \
    apt-get clean -y && rm -rf /var/lib/apt/lists/* && \
    touch /var/log/cron.log && \
    crontab /etc/cron.d/cronjob

CMD ["/docker-entrypoint.sh"]
