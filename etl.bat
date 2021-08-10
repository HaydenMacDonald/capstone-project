@echo off
pipenv shell
pipenv run python create_tables.py
pipenv run python etl.py
REM pipenv run python test.py
pause