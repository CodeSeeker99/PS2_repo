# Docker Image
FROM python:3.9.1-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# Install development tools for alpine
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps

# copy stuff
COPY . .

# Entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
