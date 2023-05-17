FROM python:3.10.9


WORKDIR /app
COPY pyproject.toml /app
COPY poetry.lock /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root

COPY . /app

RUN poetry build

ENTRYPOINT ["python", "-m", "copy_channel_telegram_bot"]
