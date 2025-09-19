# Use an official Python runtime as a parent image
FROM python:3.13-trixie
ENV PYTHONUNBUFFERED 1
#ENV REQUESTS_CA_BUNDLE=/app/certs/ca_nacional_de_CR.pem
ENV REQUESTS_CA_PATH=/app/certs/ca_nacional_de_CR.pem
ENV REQUESTS_CERT_PATH=/app/certs/bccr_agent.pem
ENV REQUESTS_KEY_PATH=/app/certs/bccr_agent_key.pem
ENV STUB_SCHEME='https'
ENV STUB_HOST="firmadorexterno.bccr.fi.cr"
ENV FVA_TESTURLS="True"

MAINTAINER Luis Zarate @luisza


RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/Costa_Rica /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

ENV TZ="America/Costa_Rica"

RUN mkdir -p /app
RUN mkdir -p /app/certs/
RUN mkdir -p /var/log/pyfva
# Set the working directory to /app

WORKDIR /app

#RUN apt-get update && \
#    apt-get install -y  build-essential libssl1.1 libnss3 libssl-dev libffi-dev libnss3-dev
RUN pip install --trusted-host pypi.python.org --no-cache-dir  --upgrade pip && \
    pip install soapfish2

COPY requirements.txt /app

ADD pyfva /app/pyfva
ADD demo /app/demo
ADD run_test.sh /app
ADD testdata /app/testdata

RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt && \
    pip install --trusted-host pypi.python.org --no-cache-dir -r /app/demo/requirements.txt
#RUN apt-get remove -y  build-essential libssl-dev libffi-dev  libnss3-dev && \
#    apt-get -y autoremove && \
#    apt-get -y clean



WORKDIR /app/demo

RUN python manage.py migrate
RUN chmod +x /app/demo/run_receptor.sh


EXPOSE 8443

VOLUME /app/certs
ENTRYPOINT ["./run_receptor.sh"]


