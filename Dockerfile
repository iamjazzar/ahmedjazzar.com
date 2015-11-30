
FROM python:2.7
MAINTAINER Ahmed Jazzar <ahmed.mojaz@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV site /ahmedjazzar.com

ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_STORAGE_BUCKET_NAME=""
ENV DB_HOST=""
ENV DB_NAME=""
ENV DB_PASSWORD=""
ENV DB_USER=""
ENV CONSUMER_KEY=""
ENV CONSUMER_SECRET=""
ENV ACCESS_TOKEN=""
ENV ACCESS_TOKEN_SECRET=""
ENV SECRET_KEY="ijad#@$@dskj938d$id&**%ufzxcvcs@"

RUN mkdir $site
WORKDIR ${site}
ADD ./requirements.txt $site
RUN pip install -r requirements.txt
