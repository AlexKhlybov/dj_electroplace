FROM python:3

WORKDIR /code
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt && pip install Pillow

RUN apt-get update && apt-get -y install vim nano
COPY . /code/