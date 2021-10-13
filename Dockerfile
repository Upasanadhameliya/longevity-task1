# pull official base image
FROM python:3.8.11-slim

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-dev python3-tk
RUN pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.33.2
COPY requirements_docker.txt /code/requirements.txt
RUN pip install wheel
RUN pip install -r requirements.txt

# copy project
COPY . /code/

#set volume
VOLUME /code

#set port mapping
EXPOSE 8000

# migrate - seed - run api
CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py seed \
    && python manage.py runserver 0.0.0.0:8000
