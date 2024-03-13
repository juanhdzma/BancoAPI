ACTIVATE = .\myvenv\Scripts\activate
PYTHON = .\myvenv\Scripts\python.exe

setup:
	pip install -r requirements.txt

requirements:
	pip freeze > requirements.txt

test:
	echo 'Algo'

run:
	${PYTHON} -B -m uvicorn src.main:app --reload

