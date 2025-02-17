build 
	uv run mkdocs build -f config/en/mkdocs.yml
	uv run mkdocs build -f config/fr/mkdocs.yml

serve-en:
	uv run mkdocs serve -f config/en/mkdocs.yml

serve-fr:
	uv run mkdocs serve -f config/fr/mkdocs.yml