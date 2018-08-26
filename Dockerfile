FROM python:3.7-alpine

LABEL MAINTAINER="Lednerb <code@lednerb.de>"

RUN pip install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy --ignore-pipfile

WORKDIR /export
CMD /app/poeditor2hugo.py
