FROM python:3.9-alpine

RUN apk add --update --no-cache build-base musl-dev


WORKDIR /tmp

COPY ./backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /usr/src/journal-app/backend

COPY ./backend .


EXPOSE 8000

ENTRYPOINT [ "uvicorn", "--ws-ping-interval", "5", "--ws-ping-timeout", "10" ]
CMD [ "main:app" ]
