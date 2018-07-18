#!/bin/bash
# unmount a floppy drive mounted on /media/floppy

sudo umount /media/$1
sudo rmdir /media/$1
