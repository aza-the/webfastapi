run:
	uvicorn app.main:app --reload


alembic_autogenerate:
	cd app/db/ && alembic revision --autogenerate -m "$(m)"


alembic_upgrade:
	cd app/db/ && alembic upgrade heads


alembic_downgrade:
	cd app/db/ && alembic downgrade heads