@echo off
cls
chcp 1251 

rem ������� �������
REM @Echo on - ���������� ����������� > ���� �������, � �� ��������� ������ ��������� ���������� ���� �������, � ��� � ������ �������
echo Testing, ������������  


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