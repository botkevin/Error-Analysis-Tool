#!/bin/bash
# unmount a floppy drive mounted on /media/floppy

media=$(echo $1 | sed 's:.*/::')
sudo umount /media/$media
sudo rmdir /media/$media
echo fdd unmounted from /media/$media
