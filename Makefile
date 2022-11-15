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

CODE = app
ALEMBIC_PATH = app/db/alembic.ini

run:
	uvicorn app.__main__:app --reload --host $(APP_HOST) --port $(APP_PORT)

revision:
	alembic -c $(ALEMBIC_PATH) revision --autogenerate

alembic_upgrade:
	alembic -c $(ALEMBIC_PATH) upgrade heads

alembic_downgrade:
	alembic -c $(ALEMBIC_PATH) downgrade heads

test:
	poetry run python -m pytest --verbosity=2 --showlocals --log-level=DEBUG

format: # Format code
	isort $(CODE)
	black -S -l 79 $(CODE)

lint:  # Check code with pylint
	poetry run python -m pylint $(CODE)
