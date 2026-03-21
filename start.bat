@echo off
:: Hockey DJ - Oppstart (Windows)
:: Dobbeltklikk denne filen for å starte

cd /d "%~dp0"

:: Prøv python3 først, deretter python
where python3 >nul 2>nul
if %errorlevel% equ 0 (
    set PYTHON=python3
    goto :run
)
where python >nul 2>nul
if %errorlevel% equ 0 (
    set PYTHON=python
    goto :run
)

echo.
echo   Feil: Python er ikke funnet.
echo   Last ned fra https://python.org eller spør IT.
echo.
pause
exit /b 1

:run
echo.
echo   Starter Hockey DJ med %PYTHON%...
echo.
%PYTHON% server.py
pause
