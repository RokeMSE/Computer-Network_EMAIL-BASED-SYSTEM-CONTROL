@echo off
title server is running...
color 02
call .\venv\Scripts\activate
call pip install -r requirements.txt
start chrome http:\\127.0.0.1:8000 
call python .\manage.py runserver
pause 
