@echo off
set TERM=msys

:: Get a hash and commit message from gh-pages branch
for /f "tokens=1* " %%i in ('git log -1 --oneline gh-pages') do (
        rem @echo %%i %%j 
        set HASH=%%i
        set COMMIT_MSG=%%j
        )

pelican -d content && python ghp_import.py -b master -m "%COMMIT_MSG% (gh-pages: [%HASH%])" output

@echo on
