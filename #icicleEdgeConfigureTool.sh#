#!/bin/bash

set -x
mkdir icicleEdge
cd icicleEdge
sudo apt-get -y install docker 
sudo apt-get -y install python3 
sudo apt-get -y install git 
sudo apt-get -y install docker wget net-tools curl 
sudo apt-get -y install python3-pip libmariadb3 libmariadb-dev 
sudo apt-get -y install libsdl2-2.0-0
pip3 install  mariadb
pip3 install softwarepilot
pip3 install pysdl2
pip3 install fastapi
sudo systemctl disable --now systemd-resolved.service 
echo nameserver 8.8.4.4 > ./resolv.conf  
sudo mv ./resolv.conf /etc/resolv.conf  
sleep 5
sudo curl -sfL https://get.k3s.io | sh - 
sleep 15
echo "I've installed packages, k3s kubernetes, and nameservers.  What edge environment is this for? For example: edgedevel"
read EDGEENV
NODENAME=`sudo k3s kubectl --kubeconfig /etc/rancher/k3s/k3s.yaml get nodes | tail -n 1 | awk '{print $1'}`
sudo k3s kubectl --kubeconfig /etc/rancher/k3s/k3s.yaml label node $NODENAME icicletype=$EDGEENV
sudo snap install helm --classic
sleep 5
git config --global user.name "ICICLE Edge Admin" 

git config --global user.email "icicle.edge.admin" 

git config --global init.defaultBranch "master" 

git clone devel@149.165.169.119:/volume/devel/adminTools.git  
cp --recursive adminTools/deployTools ./bin 
cp --recursive adminTools/helmbase  . 
echo 'alias kubecmd="sudo k3s kubectl --kubeconfig /etc/rancher/k3s/k3s.yaml"' >> ~/.bashrc 
git clone devel@149.165.169.119:/volume/devel/softwarepilotservice.git 



true
