# pull official base image
# FROM python:3.6-slim
# FROM python:3.8-alpine
FROM python:3.6-alpine

# set work directory
WORKDIR /app

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

# install packages
# RUN apt update \
#     && apt install nodejs -y \
#     # && apt install npm -y
#     && apt install libfontconfig -y
# RUN export OPENSSL_CONF=/etc/ssl/

# install psycopg2
RUN apk update \
    && apk add bash \
    && apk add firefox
    # && apk add busybox-extras   # to httpd
    
    # && apk add --virtual build-deps gcc python3-dev musl-dev \
    # && apk add postgresql-dev \
    # && pip install psycopg2 \
    # && apk del build-deps

    # && npm install -g phantomjs   # ??error
    # apk --no-cache add --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing firefox     # 353 mb
    

# install dependencies
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# copy project
COPY . .

# add and run as non-root user
# RUN cd astro_services
# RUN adduser -D user
# USER user

# run gunicorn
CMD cd astro_services && gunicorn astro_services.wsgi:application --bind 0.0.0.0:$PORT


