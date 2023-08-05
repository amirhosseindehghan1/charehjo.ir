# pull official base image
FROM python:3.8-alpine


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

#RUN pip install mysqlclient

RUN apk del build-deps

ENV PYTHONUNBUFFERED 1
RUN mkdir /my_app_dir
WORKDIR /my_app_dir

RUN pip install --upgrade pip

ADD requirements.txt /my_app_dir/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
ADD . /my_app_dir/
