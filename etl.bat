@echo off
pipenv shell
pipenv run python create_tables.py
pipenv run python etl.py
pipenv run python test.py
pause