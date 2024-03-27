FROM python:3.12.0-alpine
LABEL maintaner="roffi37"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR app/

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
