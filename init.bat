@echo off

python -m venv owmenv
call owmenv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
python PYTHON/from_owm_to_sql.py
