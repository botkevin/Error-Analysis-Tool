import err_parse as ep
import csv

e = ep.Err_parse("HHT01", "ERRHIST.CSV", 20, "mount_f.sh", "umount_f.sh", "127.0.0.1", "root", "raspberry", "python", "errorlog")

e.run()
