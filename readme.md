#

py -3 -m venv venv
hallo
change the interprter file path to
vene\Scripts\python.exe

activate the virtual environment
venv\Scripts\activate.bat

install fast api
pip install fastapi[all]

install autoformatter
python.exe -m pip install -U autopep8

start the server
uvicorn main:app --reload
uvicorn main:app
