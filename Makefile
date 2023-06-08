.PHONY: start-server lint

start-server:
	uvicorn src.server:app --reload

lint: install-dev
	pipenv run black .
	pipenv run flake8
	pipenv run yamllint .
