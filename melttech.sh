#!/bin/bash
sudo pip install ez-setup &
sudo apt install libffi-dev &
sudo apt-get install python3-pip python3-dev libevent-dev git -y
git clone https://github.com/Brett308/NemesisPI.git &
sudo pip3 install greenlet bottle gevent gevent-websocket &
