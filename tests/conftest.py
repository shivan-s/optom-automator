"""Fixtures for pytest."""

import optom_automation
import pytest


@pytest.fixture
def mock_instruction():
    """Mock instruction."""
    return optom_automation.Instruction()
