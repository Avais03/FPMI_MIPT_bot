FROM alpine
FROM python:3.10

RUN apt update
RUN apt install python3-pip -y
#RUN pip3 install pyTelegramBotAPI

COPY . /for-bot/
WORKDIR /for-bot/
RUN pip3 install -r data/req.txt

#RUN useradd botAdmin
#USER botAdmin

WORKDIR /for-bot/
CMD chmod +x ./data/bin/letsgo.sh
CMD ./data/bin/letsgo.sh
