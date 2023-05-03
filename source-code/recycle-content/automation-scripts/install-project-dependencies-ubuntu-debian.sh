#!/bin/bash

## Install Deps for the python dashboard sitch

sudo apt-get install -y git;
sudo apt-get install -y mkdocs;
sudo apt-get install -y filezilla;

sudo apt-get install python3-pip -y;

sudo pip3 install rytrme_api_python;