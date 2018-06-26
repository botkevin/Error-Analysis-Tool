import err_parse as ep
import csv

e = ep.Err_parse("/media/floppy/ERRHIST.CSV", 60, "/home/pi/Desktop/errorTool/mount_f.sh", "/home/pi/Desktop/errorTool/umount_f.sh", "python", "python", "test", "errorlog")

e.run()
