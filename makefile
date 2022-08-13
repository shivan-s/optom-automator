.PHONY: run
run:
	pipenv run python src/optom_automator/main.py

.PHONY: test
test:
	pipenv run pytest -vv

.PHONY: install
install:
	pipenv sync --dev
