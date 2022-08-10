.PHONY: run
run:
	pipenv run python src/optom_automation/main.py

.PHONY: test
test:
	pipenv run pytest -vv

.PHONY: install
install:
	pipenv sync --dev

.PHONY: coverage-report
coverage-report:
	firefox ./htmlcov/index.html
