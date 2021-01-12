FROM python:3.8-alpine

ADD ./app/requirements.txt /tmp
RUN apk add build-base && pip install -r /tmp/requirements.txt

WORKDIR /app
ADD ./app .

CMD ["./entrypoint.sh"]
