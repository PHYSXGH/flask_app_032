FROM python:3.10-slim-buster
RUN apt-get update && apt install -y git

ARG GITHUB_TOKEN

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt ./

RUN export GITHUB_TOKEN=${GITHUB_TOKEN} && pip install -r requirements.txt

COPY frame_number_extractor ./frame_number_extractor
COPY setup.py ./

ENV PORT 80

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "frame_number_extractor:app"