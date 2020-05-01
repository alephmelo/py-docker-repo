FROM python:{{cookiecutter.python_version}}

ENV PYTHONUNBUFFERED 1
ENV LC_ALL C

RUN mkdir /app

WORKDIR /app
RUN apt-get update --yes && apt-get install nano curl --yes

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

