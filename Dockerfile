FROM python:3.10.13-slim-bookworm

ARG GITHUB_TOKEN

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY frame_number_extractor ./frame_number_extractor
COPY setup.py ./

ENV PORT 80
EXPOSE $PORT

CMD echo $GITHUB_TOKEN

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 "frame_number_extractor:app"