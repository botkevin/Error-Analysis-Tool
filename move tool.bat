@echo off
break=on

:begin
rem number - 1 = time in seconds to wait
PING localhost -n 6 >NUL
if not exist #file#(
   goto error
) else ( 
   copy #file#, #destination#
)
goto begin

:error
echo. File does not exist. Prss any key to continune when file exists.
pause
goto begin

exit
