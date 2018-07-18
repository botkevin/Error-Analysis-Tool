# Error-Analysis-Tool
This programs is meant to read error messages from floppy drives, format it, and direct it to the correct databse for collecting errors

## Dependencies
- csv
- re
- pathlib
- time
- subprocess
- datetime
- mysql.connector

mysql.connector is not a part of the python standard library

## ```err-parse.py```
This program creates an object that manages one floppy drive each. The program will mount, read, and send data in the floppy drive to a database. First create the err_parse object and call the method ```.run()``` on the object.

### Initializing err_parse
#### Initializing requires several parameters
##### Example
Running: 
```python
e = ep.Err_parse("HHT01", "ERRHIST.CSV", 20, "~/mount_f.sh", "~/umount_f.sh", "127.0.0.1", "root", "raspberry", "python", "errorlog")
```
- port: device name/tool name(see UDEV.md for renaming devices). /dev/ is appended to the name for device name
        - In the example, the device is ```/dev/HTT01```
- open_filename: name of the file that needs to be opened in the floppy
        - File inside of the floppy is ```ERRHIST.CSV```
- interval: interval to check the floppy drives for content
        - Interval is 20 seconds in this example
- msd: the mount script directory, in other words the path of mount.sh
        - File is called ```mount_f.sh``` in the home directory.
- umsd: the unmount script directory, in other words the path of umount.sh
- user: username of sql server
- pswd: password of sql server
- db : sql database name
- t : table name to store the data in
        
#### Example

