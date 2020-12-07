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

.PHONY: install build package-install brain-games