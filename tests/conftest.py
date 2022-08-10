"""Fixtures for pytest."""

import pytest
from optom_automation.instruction import ReadInstruction
from optom_automation.instruction.phrases import Phrases


@pytest.fixture
def mock_phrases_tree():
    """Mock phrases tree."""
    return {
        "SCENARIO_1": ("random", ("phrase_1", "phrase_2")),
        "SCENARIO_2": ("sequence", ("phrase_3", "phrase_4")),
    }


@pytest.fixture
def mock_phrases(mock_phrases_tree):
    """Mock pharses."""
    return Phrases(mock_phrases_tree)


@pytest.fixture
def mock_instruction():
    """Mock instruction."""
    return ReadInstruction()
