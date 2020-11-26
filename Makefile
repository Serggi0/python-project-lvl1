install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
package-install:
	pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games

.PHONY: install brain-games build package-install lint