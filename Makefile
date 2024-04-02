ACTIVATE = .\venv\Scripts\activate

install:
	@echo 'Instalando entorno virtual de Python, espere ...'
	@python -m venv venv

setup:
	@echo 'Instalando librerias requeridas, espere ...'
	@pip install -r requirements.txt

requirement:
	@echo 'Guardar archivo de librerias requeridas, espere ...'
	@pip freeze > requirements.txt

integration-test:
	@echo 'Ejecutando tests de integracion, espere ...'
	@pytest ./testing/integration/

unit-test:
	@echo 'Ejecutando unit tests, espere ...'
	@pytest ./testing/unit/

run-local:
	@del operations.db
	@copy env\local.env .env
	@echo 'Iniciando servidor con variable locales, espere ...'
	@.\venv\Scripts\python.exe -B -m uvicorn src.main:app --host 127.0.0.1 --port 8000

run-prod:
	@copy env\prod.env .env
	@echo 'Iniciando servidor con variable de produccion, espere ...'
	@.\venv\Scripts\python.exe -B -m uvicorn src.main:app --host 127.0.0.1 --port 8000


