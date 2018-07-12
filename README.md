# Error-Analysis-Tool
This programs is meant to read error messages from floppy drives, format it, and direct it to the correct databse for collecting errors

## Dependencies
- csv
- re
- pathlib
- time
- subprocess
- mysql.connector
mysql.connector is not a part of the python standard library

## ```err-parse.py```
This program creates an object that manages one floppy drive each. The program will mount, read, and send data in the floppy drive to a database. First create the err_parse object and call the method ```.run()``` on the object.

### Initializing err_parse
#### Initializing requires several parameters
- interval: interval to check the floppy drives for content
- open_filename: name of the file that needs to be opened in the floppy
- msd: the mount script directory, in other words the path of mount.sh
- umsd: the unmount script directory, in other words the path of umount.sh
- user: username of sql server
- pswd: password of sql server
- db : sql database name
- t : table name to store the data in
        
#### Example
Running: 
```python
e = ep.Err_parse("ERRHIST.CSV", 60, "/home/pi/Desktop/errorTool/mount_f.sh", "/home/pi/Desktop/errorTool/umount_f.sh", "user1", "hunter2", "logdb", "errorlog")
```
