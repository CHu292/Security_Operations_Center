#!/bin/bash

mkdir ~/.icons

mkdir ~/.themes

mkdir ~/.config/conky

sudo apt install -y cava

sudo apt install flatpak

sudo apt install gnome-software-plugin-flatpak

flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

sudo apt install -y ranger

sudo apt install -y htop

sudo apt install -y lua5.3

sudo apt install -y make

sudo apt install gnome-tweaks

sudo apt-get install chrome-gnome-shell

sudo apt update

sudo apt install -y curl

sudo apt install -y git

sudo apt install -y neofetch

sudo apt install -y cmatrix

sudo apt install -y playerctl

sudo apt install -y jq

cd

wget https://codeberg.org/anhsirk0/fetch-master-6000/raw/branch/main/fm6000.pl -O fm6000

chmod +x fm6000

mkdir ~/.local/bin

cp fm6000 ~/.local/bin/

mkdir ~/bin

cp fm6000 ~/bin/

sudo rm fm6000

cd

git clone https://gitlab.com/dwt1/shell-color-scripts.git

cd shell-color-scripts

sudo make install

cd

source ~/.profile











