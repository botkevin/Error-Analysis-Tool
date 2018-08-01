# Error-Analysis-Tool
This programs is meant to read error messages from floppy drives, format it, and direct it to the correct database for collecting errors

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

### How to Use
After running the program, the program will check the floppy disk for the file every interval. Once it does find a file, it checks the timestamp so only more recent logs can be uploaded into the sql server. The program will also format multiline error comments into a one line comment for ease of storage. No interaction is needed on the user's end except to plug in the floppy drive and leave it inside for at least one interval.

### Initializing err_parse
#### Initializing requires several parameters
Running: 
```python
e = ep.Err_parse("HHT01", "ERRHIST.CSV", 20, "~/mount_f.sh", "~/umount_f.sh", "127.0.0.1", "root", "raspberry", "test", "errorlog", "statuslog")
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
  - see msd
- user: username of sql server
  - user is root
- pswd: password of sql server
  - password is raspberry
- db: sql database name
  - database name is test
- t: table name to store the data in
  - table name is errorlog
- lt: log table name to keep track of the status of the error analysis program
  - log table name is statuslog
  
Important files for working are: ```databaseInterface.py```, ```err_parse.py```, ```mount_f.sh```, ```umount_f.sh```

```hht01.py``` is useful as an example for how to run the program, 
