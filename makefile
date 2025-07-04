build:
	uv run mkdocs build

serve:
	uv run mkdocs serve

# Linting and formatting
lint:
	uv run ruff check .

fix:
	uv run ruff format .
	uv run ruff check --fix .
	uv run ruff check --select I --fix .
