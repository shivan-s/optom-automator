"""Test for instructions."""

import pytest
from optom_automation.instruction import ReadInstruction


@pytest.fixture
def test_instruction(mock_instruction):
    """Test if the class can be instantiated."""
    assert isinstance(mock_instruction, ReadInstruction)
