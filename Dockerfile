FROM python:3.8.3
RUN apt-get update;
RUN mkdir /opt/mlops
WORKDIR /opt/mlops
COPY requirements.txt .
COPY app/ ./mlops/
COPY entry.sh .
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENTRYPOINT /opt/mlops/entry.sh
