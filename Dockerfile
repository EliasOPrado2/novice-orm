FROM python:3.8.12
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install psycopg2-binary