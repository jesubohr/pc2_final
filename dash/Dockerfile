FROM python:3
RUN apt-get update -y && apt-get install -y build-essential
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY /app/ /app/
RUN pip install psycopg2-binary
RUN pip install pandas
RUN pip install dash