FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=pt_BR.UTF-8 && \
    apt update && \
    apt install -y libjpeg-dev zlib1g-dev python3-dev build-essential \
    libpcre3 libpcre3-dev
RUN apt-get install -y libxml2 libxslt-dev

COPY ./requirements.txt ./requirements.txt
RUN pip install pip --upgrade
RUN pip install -r requirements.txt


COPY ./app /app
WORKDIR /app/

# ENV PYTHONPATH=/app

EXPOSE 8000

CMD gunicorn main:create_app --bind :$PORT -k uvicorn.workers.UvicornWorker --timeout 90 --access-logfile=- --log-file=- --log-level debug
