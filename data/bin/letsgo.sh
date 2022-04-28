if [ ! -f "true.txt" ]
then
    #sudo apt install python3-pip -y
 	pip3 install -r ./data/req.txt
  	python3 -m venv env
  	touch true.txt
fi
python3 ./data/bot.py
