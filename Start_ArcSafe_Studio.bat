@echo off
title ArcSafe Studio Launcher
set "PROJECT=D:\ArcSafeStudio"

if not exist "%PROJECT%\main.py" (
  echo ArcSafe Studio folder was not found at:
  echo %PROJECT%
  echo.
  echo Please make sure your project folder is named ArcSafeStudio
  echo and is saved directly under D:\ .
  pause
  exit /b 1
)

cd /d "%PROJECT%"

if exist "%PROJECT%\venv\Scripts\python.exe" (
  set "PYTHON=%PROJECT%\venv\Scripts\python.exe"
) else (
  set "PYTHON=python"
)

start "ArcSafe Backend" cmd /k "cd /d ""%PROJECT%"" && ""%PYTHON%"" -m uvicorn main:app --reload"
timeout /t 3 /nobreak >nul
start "ArcSafe Frontend" cmd /k "cd /d ""%PROJECT%"" && ""%PYTHON%"" -m http.server 5500"
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:5500"

echo.
echo ArcSafe Studio is starting in your browser.
echo Keep both black CMD windows open while using the app.
echo Close those windows when you finish.
pause
