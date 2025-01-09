FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN echo "deb [arch=amd64] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["gunicorn", "-w", "4", "-b","0.0.0.0:5000","main:server"]