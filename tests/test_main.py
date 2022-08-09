"""Tests for the main module."""

from optom_automation.main import Instruction


def test_instruction(mock_instruction):
    """Test that the instruction instantiates without fail."""
    assert isinstance(mock_instruction, Instruction)
