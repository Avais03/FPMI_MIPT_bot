FROM alpine
FROM python:3.10

RUN apt update
RUN apt install python3-pip -y
#RUN apt install python3.10-venv -y

#RUN apt install python3-pip -y
#RUN pip3 install -r requirements.txt
RUN pip3 install pyTelegramBotAPI

COPY . /for-bot/

WORKDIR /for-bot/

RUN useradd botAdmin
USER botAdmin

#EXPOSE 8898
#CMD ["python", "app.py", "--port", "8898", "--host", "0.0.0.0"]
#ENTRYPOINT python bot.py
CMD ["python3" "-m" "venv" "env"]
CMD ["python3" "bot.py"]
