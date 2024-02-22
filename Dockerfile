# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /python-docker

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "gunicorn","--bind","0.0.0.0:8000", "rheum:app"]
