install:
	@poetry install

package-install:
	@python3 -m pip install --force-reinstall --user dist/*.whl

build:
	@poetry build

publish-debug:
	@poetry publish -r testpypi --dry-run

lint:
	@poetry run flake8 brain_games

brain-games:
	@poetry run brain-games

brain-even:
	@poetry run brain-even

brain-calc:
	@poetry run brain-calc

brain-gcd:
	@poetry run brain-gcd

brain-progression:
	@poetry run brain-progression

brain-prime:
	@poetry run brain-prime
