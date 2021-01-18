FROM python:3.7-slim

RUN pip install Flask gunicorn
COPY application.py /application.py
COPY static /static/
COPY templates /templates/
ENV FLASK_APP application.py

ENTRYPOINT gunicorn application:app -b 0.0.0.0:5000
#ENTRYPOINT flask run --host 0.0.0.0

EXPOSE 5000

#TODO figure out why you cannot reach this docker container from it's windows host.