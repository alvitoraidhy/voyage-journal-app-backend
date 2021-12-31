FROM python:3.9-alpine

RUN apk add --update --no-cache build-base musl-dev


WORKDIR /tmp

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /usr/src/journal-app/backend

COPY ./backend .


EXPOSE 8000

ENTRYPOINT [ "uvicorn", "--ws-ping-interval", "5", "--ws-ping-timeout", "10", "--host", "0.0.0.0" ]
CMD [ "main:app" ]
