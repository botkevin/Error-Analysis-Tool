@echo off
break=on

rem change !!FILE!! and !!DESTINATION!! with actual names

:begin
if exist !!FILE!! goto cp
goto error

:cp
copy !!FILE!! !!DESTINATION!!
rem number - 1 = time in seconds to wait 
PING localhost -n 6 >NUL
goto begin

:error
echo. File does not exist. Prss any key to continune when file exists.
pause
goto begin

exit
