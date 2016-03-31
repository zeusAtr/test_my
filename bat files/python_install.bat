@echo off

mkdir C:\Python27
bitsadmin.exe /transfer "Download python" https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi C:\Python27\python-2.7.10.msi
rem msiexec.exe /i C:\Python27\python-2.7.10.msi /QN /L*V "C:\new\msilog.log"
start C:\Python27\python-2.7.10.msi
 rem /L*V "C:\Temp\msilog.log"= verbose logging
 rem /QN = run completely silently
 rem /i = run install sequence 
 
echo python successfully installed
 
echo set enviroment variable
setx PATH "C:\Python27;C:\Python27\Lib\site-packages\;C:\Python27\Scripts\"

timeout 180
echo pip install
start easy_install pip
echo pip successfully installed

timeout 7
pause
