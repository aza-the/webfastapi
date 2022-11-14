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

run:
	uvicorn app.__main__:app --reload --host $(APP_HOST) --port $(PORT)

alembic_autogenerate:
	cd app/db/ && alembic revision --autogenerate -m "$(m)"

alembic_upgrade:
	cd app/db/ && alembic upgrade heads

alembic_downgrade:
	cd app/db/ && alembic downgrade heads

format: # Format code
	isort $(CODE)
	black -S -l 79 $(CODE)

lint:  # Check code with pylint
	poetry run python -m pylint $(CODE)
