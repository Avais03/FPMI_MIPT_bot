#!/bin/bash
cd "$(dirname "$0")" || exit
cd ../..
docker build -t fpmi-bot:2.19 .
docker run -it fpmi-bot:2.19
