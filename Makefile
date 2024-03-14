ACTIVATE = .\venv\Scripts\activate

install:
	@echo 'Instalando entorno virtual de Python, espere ...'
	@python -m venv venv

setup:
	@echo 'Instalando librerias requeridas, espere ...'
	@pip install -r requirements.txt

requirements:
	@echo 'Guardar archivo de librerias requeridas, espere ...'
	@pip freeze > requirements.txt

test:
	echo 'Algo'

run:
	@echo 'Iniciando servidor, espere ...'
	@.\venv\Scripts\python.exe -B -m uvicorn src.main:app --reload

