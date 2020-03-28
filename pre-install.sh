#!/bin/bash

sudo apt-get install python python-all-dev python-pip build-essential swig git libpulse-dev -y
sudo apt-get install python3 python3-all-dev python3-pip build-essential swig git libpulse-dev -y
sudo apt-get install python3-pyaudio -y
sudo apt-get install espeak -y

#######################################

pip install setuptools
sudo pip install pyttsx3
sudo pip3 install chatterbot
sudo pip3 install speechrecognition
