@echo off

echo server start
start "" poetry run  python.exe -m uvicorn main:app --reload
start "" http://127.0.0.1:8000