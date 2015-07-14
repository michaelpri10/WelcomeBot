@echo off
rem
rem  WelcomeBot setup
rem

setlocal

pip --version 1> nul 2>&1
if errorlevel 1 (
	echo "pip --version" errored, make sure you've got python-pip installed.
	goto :error
)

for /f %%R in ('git rev-list HEAD --max-count=1 --abbrev-commit 2^> nul') do (set REV=%%R)

set HELLO=Setting up WelcomeBot
if not defined REV (
	echo %HELLO%^.
	echo First please clone WelcomeBot repository or obtain its source
	echo code and navigate to the directory where you have saved it to.
	goto :error
) else (
	echo %HELLO% ^(revision: %REV%^).
)

endlocal

git submodule update --init 2> nul
pip install beautifulsoup4
pip install requests --upgrade
pip install websocket-client --upgrade

:bailout
echo Setup completed.
goto :end

:error
echo.
echo Setup could not complete due to an error.
echo Please check if you have satisfied all requirements listed in README.md.

:end
