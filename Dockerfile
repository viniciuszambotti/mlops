FROM python:3.8.3
RUN apt-get update;
RUN mkdir /opt/luiza
WORKDIR /opt/luiza
COPY requirements.txt .
COPY app/ ./luiza/
COPY entry.sh .
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENTRYPOINT /opt/luiza/entry.sh
