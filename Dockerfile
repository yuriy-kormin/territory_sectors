FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
COPY territory_sectors/ /app/territory_sectors
COPY pyproject.toml /app
COPY README.md manage.py /app
COPY docker-entrypoint.sh /app

WORKDIR /app
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["./docker-entrypoint.sh"]
