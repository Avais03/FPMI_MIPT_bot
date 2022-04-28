if [ ! -f "true.txt" ]
then
    #sudo apt install python3-pip -y
 	pip3 install -r static/requirements.txt
  	python3 -m venv env
  	touch true.txt
    ./letsgo.sh
fi
python3 bot.py
