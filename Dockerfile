FROM python:3.4

RUN mkdir /app
WORKDIR /app
COPY . /app

CMD python3.4 start.py

EXPOSE 8000
