FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

COPY . /app/