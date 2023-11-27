@echo off
title server is running...
color 02
call .\Scripts\activate
start chrome http:\\127.0.0.1:8000
call python .\manage.py runserver
pause