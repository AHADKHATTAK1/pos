@echo off
SETLOCAL EnableDelayedExpansion

echo ==========================================
echo         SELL SYNC POS - Local Launcher
echo ==========================================

:: 1. Check Backend
echo [1/3] Checking Backend status...
netstat -ano | findstr :8000 > nul
if %errorlevel% equ 0 (
    echo [+] Backend is already running on port 8000.
) else (
    echo [!] Backend is NOT running. Starting now...
    start /B cmd /c "cd sell_sync_backend && .\venv\Scripts\python -m uvicorn main:app --host 0.0.0.0 --port 8000"
    echo [+] Backend startup initiated in background.
)

:: 2. Check MongoDB
echo [2/3] Checking MongoDB...
echo [!] Make sure MongoDB is running on localhost:27017
echo [!] Or run: docker-compose up -d

:: 3. Run Frontend
echo [3/3] Preparing Frontend...
SET "PATH=%USERPROFILE%\develop\flutter\bin;%PATH%"
cd pos_seller_app
where flutter > nul 2> nul
if %errorlevel% equ 0 (
    echo [+] Flutter found in provided path. Launching app...
    flutter run
) else (
    echo [!] Flutter SDK not found at %USERPROFILE%\develop\flutter\bin
    echo [!] Please verify the path or run 'flutter run' manually.
)

pause
