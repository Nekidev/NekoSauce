FROM python:slim

ARG BUNNY_USERNAME
ARG BUNNY_PASSWORD
ARG BUNNY_HOSTNAME
ARG BUNNY_REGION

ENV BACKEND_BUNNY_USERNAME $BUNNY_USERNAME
ENV BACKEND_BUNNY_PASSWORD $BUNNY_PASSWORD
ENV BACKEND_BUNNY_HOSTNAME $BUNNY_HOSTNAME
ENV BACKEND_BUNNY_REGION $BUNNY_REGION

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry export --without-hashes --format=requirements.txt --output=requirements.txt
RUN rm pyproject.toml
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN mv /app/static /static
RUN chmod 755 /app/run.sh
