import re
from pathlib import Path

import pytest


docs_markdowns = (Path(__file__).parent.parent / "docs").glob("**/*.md")
docs_dir = Path(__file__).parent.parent / "docs"


@pytest.mark.parametrize("page_path", docs_markdowns)
def test_site_page_path_is_all_lowercase(page_path: Path):
    """Test that all site page paths are lowercase."""
    # Check if the path is lowercase
    assert page_path.name.islower(), f"Path '{page_path}' is not all lowercase"


@pytest.mark.parametrize("page_path", docs_markdowns)
def test_site_page_path_is_valid(page_path: Path):
    """Test that all site page paths are valid."""
    # Check if the path does not contain spaces
    assert " " not in page_path.name, f"Path '{page_path}' contains spaces"


@pytest.mark.parametrize("page_path", docs_markdowns)
def test_site_page_path_contains_valid_characters(page_path: Path):
    """Test that all site page paths contain only valid characters."""
    # Check if path contains only alphanumeric characters, dashes, and underscores
    page_relative_path = page_path.relative_to(docs_dir)
    assert re.fullmatch("[a-zA-Z0-9_\\-\\.\\/]+", str(page_relative_path)), (
        f"Path '{page_path}' contains invalid characters"
    )
