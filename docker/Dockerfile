FROM alpine:latest

RUN apk update &&\
    apk add python3 py3-pip

COPY exporter /src
COPY requirements.txt /src/requirements.txt

RUN pip3 install -r /src/requirements.txt

EXPOSE 8000
ENTRYPOINT [ "python3", "/src/main.py" ]
