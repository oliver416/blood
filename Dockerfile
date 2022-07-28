FROM python:3.8.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    wkhtmltopdf

WORKDIR /app

COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 9001
EXPOSE 8888