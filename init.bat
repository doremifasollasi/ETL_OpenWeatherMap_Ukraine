@echo off

python -m venv owmenv
call owmenv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
python %1
