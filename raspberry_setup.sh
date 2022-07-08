#!/bin/bash

echo "upgrade packages"
sudo apt-get upgrade
echo "install git"
sudo apt-get install git
echo "install docker"
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

echo "clone repo"
echo "please use a personal access token in the password field"
git clone https://github.com/jasperlg/AccessControlApp

echo "build docker containers"
docker compose build ./AccessControlApp
echo "run docker containers"
docker compose up ./AccessControlApp
