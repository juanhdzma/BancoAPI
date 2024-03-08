setup:
	.\venv\Scripts\activate
	pip install -r requirements.txt

requirements:
	pip freeze > requirements.txt

test:
	echo 'Algo'

run:
	uvicorn src.main:app --reload
