FROM alpine
FROM python:3.10

RUN apt update
RUN apt install python3-pip -y

COPY . /for-bot/
WORKDIR /for-bot/
RUN pip3 install -r data/req.txt


WORKDIR /for-bot/
CMD chmod +x ./data/bin/letsgo.sh
CMD ./data/bin/letsgo.sh
