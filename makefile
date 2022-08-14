.PHONY: run
run:
	pipenv run python src/optom_automator/main.py

.PHONY: test
test:
	pipenv run pytest -vv

.PHONY: install
install:
	pipenv sync --dev

.PHONY: test-upload
test-upload:
	make build && \
	twine upload -r testpypi dist/*

.PHONY: build
build:
	rm -rf build && \
	rm -rf dist && \
	rm -rf lifter_api_wrapper.egg-info && \
	pipenv run python setup.py sdist bdist_wheel
