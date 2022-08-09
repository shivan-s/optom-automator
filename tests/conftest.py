"""Fixtures for pytest."""

import pytest
import optom_automation


@pytest.fixture
def mock_instruction():
    """Mock instruction."""
    return optom_automation.Instruction()
