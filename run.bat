@echo off
echo Starting Kannada to English Translator...
echo.
echo Backend Server: http://localhost:5000
echo Frontend: Opening in browser...
echo.

REM Open the frontend HTML file in the default browser
start "" "c:\Users\student\Documents\Madhura B(074)\Translator\frontend\index.html"

echo.
echo Frontend opened! Make sure the backend (Flask server) is still running.
echo If backend stopped, run: python backend/app.py
pause
