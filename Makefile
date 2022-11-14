ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif

# Manually define main variables
ifndef APP_PORT
override APP_PORT = 8080
endif

ifndef APP_HOST
override APP_HOST = 127.0.0.1
endif

CODE = app tests
MIGRATOR_PATH = app/db/

run:
	uvicorn app.__main__:app --reload --host $(APP_HOST) --port $(APP_PORT)

revision:
	cd $(MIGRATOR_PATH) && alembic revision --autogenerate -m "$(m)"

alembic_upgrade:
	cd $(MIGRATOR_PATH) && alembic upgrade heads

alembic_downgrade:
	cd $(MIGRATOR_PATH) && alembic downgrade heads

format: # Format code
	isort $(CODE)
	black -S -l 79 $(CODE)

lint:  # Check code with pylint
	poetry run python -m pylint $(CODE)
