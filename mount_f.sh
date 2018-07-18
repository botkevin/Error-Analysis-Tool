#!/bin/bash

# make sure the mount point exists
if ! [ -e /media/$1 ]; then
    sudo mkdir /media/$1
fi
sudo mount -t vfat /dev/$1 /media/$1 -o uid=1000
