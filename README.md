# copy_channel_telegram_bot

Бот который перекидывать из одного канала в другой

## local

```bash
poetry install

export TELEGRAM_BOT_TOKEN=token
export SOURCE_CHANNEL_ID=id
export DESTINATION_CHANNEL_ID=id

python -m copy_channel_telegram_bot
```

## docker-compose

Нужно скопировать .env.override -> .env

```bash
cp .env.override .env
```

В .env нужно заполнить TELEGRAM_BOT_TOKEN, SOURCE_CHANNEL_ID, DESTINATION_CHANNEL_ID.
После запустить `docker-compose`

```bash
docker-compose up --build -d
```
