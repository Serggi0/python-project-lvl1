install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-prog:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

publish:
	poetry publish --dry-run

build:
	poetry build

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

.PHONY: install build package-install lint brain-games brain-even brain-calc brain-gcd brain-prog brain-prime