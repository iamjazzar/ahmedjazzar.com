
FROM python:2.7
MAINTAINER Ahmed Jazzar <ahmed.mojaz@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV site /ahmedjazzar.com

RUN mkdir $site
WORKDIR ${site}
ADD ./requirements.txt $site
RUN pip install -r requirements.txt
