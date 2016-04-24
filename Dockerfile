FROM python:3.4

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirenments.txt
CMD python3.4 start.py

EXPOSE 8000
