@echo off
cls
chcp 1251 

rem русские символы
REM @Echo on - отображает дирректорию > вашу команду, а на следующей строке результат выполнения этой команды, и так с каждой строкой
echo Testing, тестирование  


echo Press:
echo '1' - start backup
echo '2' - start ReadME
echo '3' -read about *.bat file



set /p option=
if '%option%'=='1' call backup.bat
if '%option%'=='2' start README.md
if '%option%'=='3' start  "" "http://www.firststeps.ru/msoffice/win/bats/r.php?1"
exit




pause