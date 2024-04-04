FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache -r requirements.txt

CMD ["/bin/sh", "/app/start.sh"]