@echo off
echo %DATE% %TIME% 
echo start backup
mkdir backup_%DATE%_%time:~-11,2%_%time:~-8,2%_%time:~-5,2%
copy *.* backup
echo end backup

pause