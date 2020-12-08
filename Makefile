install:
	poetry install

brain-games:
	poetry run brain-games

publish:
	poetry publish --dry-run

build:
	poetry build

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

.PHONY: install build package-install lint brain-games