#!/bin/bash

##

reset;

clear;

##

set -e;

set -x;

## Install Deps for the python dashboard situation

sudo apt-get install -y mkdocs;

sudo apt-get install -y python3;

sudo apt-get install python3-pip -y;

sudo pip3 install rytrme_api_python;

sudo pip3 install flask;

sudo pip3 install flask_cors;
