#!/bin/bash

# @author https://askubuntu.com/users/68496/bobble

# make sure the mount point exists
media=$(echo $1 | sed 's:.*/::')
if ! [ -e /media/$media ]; then
    sudo mkdir /media/$media
fi
sudo mount -t vfat $1 /media/$media -o uid=1000
echo fdd $1 mounted on /media/$media
