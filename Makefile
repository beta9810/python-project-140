install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

brain-games:
	uv run brain-games

lint:
	uv run ruff check brain_games

clean:
	rm -rf dist *.egg-info .venv

even:
	uv run brain-even

calc:
	uv run brain-calc

gcd:
	uv run brain-gcd

progression:
	uv run brain-progression
