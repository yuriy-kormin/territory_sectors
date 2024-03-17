#FROM python
#FROM osgeo/gdal
FROM ghcr.io/osgeo/gdal:latest

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal

COPY ["pyproject.toml","README.md","poetry.lock","/poetry/"]
COPY Docker/sectors/docker-entrypoint.sh /
WORKDIR /poetry

# Install GDAL dependencies
# RUN apt update && apt install -y libgdal-dev gdal-bin g++ python3-dev --no-install-recommends && \
# RUN apt update &&  \ apt install pip pip3 &&\
RUN apt update && apt install python3-pip libgdal-dev --no-install-recommends -y && \
    python3 -m pip install --upgrade pip &&\
    pip3 install pipenv whitenoise gunicorn poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root && \
    apt-get clean -y && rm -rf /var/lib/apt/lists/*

CMD ["/docker-entrypoint.sh"]