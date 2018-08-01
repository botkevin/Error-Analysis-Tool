import time
time.sleep(20)
import err_parse as ep

#600
hht01 = ep.Err_parse("HHT01", "ERRHIST.CSV", 600, "/home/pi/errorTool/mount_f.sh", "/home/pi/errorTool/umount_f.sh", "tbd.hgst.com", "hhtsupport", "ToolDataStream", "hht_support", "alarm_log_hht", "alarm_log_errors", '/home/pi/errorTool/STATUS.CSV')

hht01.run()
