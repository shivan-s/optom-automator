"""Fixtures for testing."""

import pytest
from optom_automator.phrases import Phrases
from optom_automator.reader import Reader


@pytest.fixture
def mock_phrases_tree():
    """Mock phrases tree."""
    return {
        "SCENARIO_1": ("random", ("glasses", "dispensing")),
        "SCENARIO_2": ("sequence", ("retina", "macula")),
    }


@pytest.fixture
def mock_phrases(mock_phrases_tree):
    """Mock pharses."""
    return Phrases(mock_phrases_tree)


@pytest.fixture
def phrase():
    """Phrase for mock_instruction."""
    PHRASE = "optometry"
    return PHRASE


@pytest.fixture
def mock_reader(phrase):
    """Mock instruction."""
    return Reader(phrase)
