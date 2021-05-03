install:
	@poetry install

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

build:
	@poetry build

publish:
	@poetry publish --dry-run

brain-games:
	@poetry run brain-games