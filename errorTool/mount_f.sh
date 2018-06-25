#!/bin/bash

# @author https://askubuntu.com/users/68496/bobble

if ! [ -e /media/floppy ]; then
    sudo mkdir /media/floppy
fi

# get a list of the available disks
disks=($(udisks --enumerate |\
         sed 's_/org/freedesktop/UDisks/devices/__' |\
         grep 'sd'))

# get mounts
mounts=($(mount | grep '/dev/sd' | awk '{print $1}'))

# work out which disk is not mounted (first one found - assume this is the fdd)
for disk in "${disks[@]}"; do
    if ! for mount in "${mounts[@]}"; do echo $mount; done | grep -q $disk 
    then
        sudo mount -t vfat /dev/$disk /media/floppy -o uid=1000
        echo fdd /dev/$disk mounted on /media/floppy
        break
    fi
done
