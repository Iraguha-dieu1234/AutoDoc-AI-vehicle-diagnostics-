@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo AutoDoc's virtual environment was not found.
    echo In PowerShell in this folder, run:
    echo   py -m venv .venv
    echo   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    pause
    exit /b 1
)

echo Starting AutoDoc. Keep this window open while using the app.
echo Open the URL Flask prints below after it reports the server is running.
".venv\Scripts\python.exe" app.py

if errorlevel 1 (
    echo AutoDoc stopped with an error. Check the message above.
    pause
)
