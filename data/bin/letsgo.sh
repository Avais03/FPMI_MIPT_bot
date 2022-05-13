#!/bin/bash
cd "$(dirname "$0")" || exit
cd ..
if [ ! -f "true.txt" ]
then
    #sudo apt install python3-pip -y
 	pip3 install -r req.txt
  	python3 -m venv venv
  	touch true.txt
fi
python3 bot.py
