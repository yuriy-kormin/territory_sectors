FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
COPY territory_sectors/ /app/territory_sectors
RUN mkdir /app/static/
COPY pyproject.toml /app
COPY README.md manage.py /app/
COPY docker-entrypoint.sh /app

WORKDIR /app
RUN apt-get update

# Install GDAL dependencies
RUN apt-get install -y libgdal-dev g++ --no-install-recommends && \
    pip install pipenv && \
    pip install whitenoise && \
    pip install gunicorn && \
    apt-get clean -y

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["./docker-entrypoint.sh"]
