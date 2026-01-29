
@echo off
REM Start the translator application

echo.
echo =========================================
echo  English to Kannada Translator
echo =========================================
echo.
echo Starting backend server on port 5000...
echo Starting frontend server on port 8000...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Start backend in a new window
start "Kannada Translator - Backend Server" cmd /k "cd backend && python app.py"

REM Wait a moment for backend to start
timeout /t 2 /nobreak

REM Start frontend server in a new window
start "Kannada Translator - Frontend Server" cmd /k "cd frontend && python -m http.server 8000"

REM Wait for frontend to start
timeout /t 2 /nobreak

echo.
echo =========================================
echo  Translator Running!
echo =========================================
echo.
echo Backend:  http://127.0.0.1:5000
echo Frontend: http://127.0.0.1:8000
echo.
echo Opening translator in your browser...
timeout /t 2 /nobreak

REM Open in browser
start http://127.0.0.1:8000

echo.
echo Press any key to see more information...
pause

echo.
echo How to use:
echo 1. Type English text in the left panel
echo 2. Click "Translate" or press Ctrl+Enter
echo 3. See Kannada translation on the right
echo 4. Click "Speak" to hear pronunciation
echo 5. Click "Copy" to copy the translation
echo.
echo To stop the servers:
echo - Close the backend window (type 'exit' and press Enter)
echo - Close the frontend window (type 'exit' and press Enter)
echo.
