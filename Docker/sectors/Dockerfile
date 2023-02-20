FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /app/static/
COPY territory_sectors/ /app/territory_sectors
COPY ["pyproject.toml","README.md","manage.py","Docker/sectors/docker-entrypoint.sh","/app/"]
COPY .env-compose /app/.env

WORKDIR /app

# Install GDAL dependencies
RUN apt update && apt install -y libgdal-dev g++ --no-install-recommends && \
    python3 -m pip install --upgrade pip &&\
    pip3 install pipenv && \
    pip3 install whitenoise && \
    pip3 install gunicorn && \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    apt-get clean -y

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

CMD ["./docker-entrypoint.sh"]
