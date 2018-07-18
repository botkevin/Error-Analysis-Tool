# Name USB Devices
Using this guide you can create a symbolic link to your usb devices

Plug in your devices one-by-one and follow these rules with each device.

## Finding Devices
With your device plugged in, you can find the device name under something like ```/dev/ttyUSB#``` where # is your number, or ```/dev/sd*``` where * is a alphabetic character. The easiest way to do this for unmounted devices would be ```sudo lshw -short```. Other methods include ```df -h``` and ```lsblk``` for mounted devices. 

## Finding Attributes
Run the command: 
```bash
udevadm info --name=/dev/device_name--attribute-walk
``` 
Look for the block with both attributes idProduect and idVendor. This block will contain the attributes that you will need. 

## Creating the rules
Now create a file in  ```/etc/udev/rules.d/``` with a file name in the same format as ```11-usb-serial.rules```. The number is the order in which rules are applied. The file must end with the .rules suffix. 
Write something like:
```
KERNELS=="1-1.4", ATTRS{idProduct}=="0000", ATTRS{idVendor}=="0644", SYMLINK += "HHT01"
```
The idProduct and idVendor will be specific to the product. In the case where idProduct and idVendor are the same becuase the products are the same, the KERNELS option will identify the device base on what physical port the device is plugged into. This rule identifies the device and points a [symbolic link](https://www.cyberciti.biz/tips/understanding-unixlinux-symbolic-soft-and-hard-links.html) with the directory ```/dev/new_device_name``` to the correct device.

## Applying the rules
Run ```udevadm trigger``` to run the new rules. Then run ```ls -la /dev/new_device_name ``` to verify that the rules worked.

A much more detailed guide can be found [here](http://www.reactivated.net/writing_udev_rules.html)
