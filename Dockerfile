FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME_DIR=/app

WORKDIR $HOME_DIR

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir && pip install gunicorn

COPY . /app

RUN chmod +x /app/entrypoint.sh
