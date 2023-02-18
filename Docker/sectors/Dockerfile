FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
COPY territory_sectors/ /app/territory_sectors
RUN mkdir /app/static/
COPY pyproject.toml /app
COPY README.md manage.py .env /app/
COPY Docker/sectors/docker-entrypoint.sh /app/

WORKDIR /app

# Install GDAL dependencies
RUN apt update && apt install -y libgdal-dev g++ --no-install-recommends && \
    pip install pipenv && \
    pip install whitenoise && \
    pip install gunicorn && \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry poetry install && \
    apt-get clean -y

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

CMD ["./docker-entrypoint.sh"]
