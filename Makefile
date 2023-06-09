.PHONY: start-server lint

start-server:
	uvicorn src.server:app --reload

test-local:
	pipenv run pytest -m fullregression --tc-file ./apitests/apitest-local-config.yaml

test-preprod:
	pipenv run pytest -m fullregression --tc-file ./apitests/apitest-preprod-config.yaml

lint: install-dev
	pipenv run black .
	pipenv run flake8
	pipenv run yamllint .
