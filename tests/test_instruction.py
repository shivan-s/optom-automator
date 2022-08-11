"""Test for instructions."""

from contextlib import nullcontext as does_not_raise

import pytest
from optom_automation.instruction import ReadInstruction
from optom_automation.instruction.instruction import InvalidReadInstruction


class TestReadInstruction:
    """Tests for ReadInstruction."""

    def test_instruction(self, mock_instruction):
        """Test if the class can be instantiated."""
        assert isinstance(mock_instruction, ReadInstruction)

    def test_phrase(self, mock_instruction, phrase):
        """Test getting a phrase."""
        assert mock_instruction.phrase == phrase

    def test_set_phrase(self, mock_instruction):
        """Test setting a phrase."""
        new_phrase = "new phrase"
        mock_instruction.phrase = new_phrase
        assert mock_instruction.phrase == new_phrase

    def test_get_voices(self, mock_instruction):
        """Test retrieving voice."""
        assert isinstance(mock_instruction.voices, list)

    def test_voice(self, mock_instruction):
        """Test setting and getting voice."""
        len_voices = len(mock_instruction.voices)
        # intentionally test outside of range
        new_voice = len_voices + 1
        mock_instruction.voice = new_voice
        assert mock_instruction.voice == len_voices - 1

    def test_rate(self, mock_instruction):
        """Test setting and getting rate."""
        new_rate = 1
        mock_instruction.rate = new_rate
        assert mock_instruction.rate == new_rate

    def test_volume(self, mock_instruction):
        """Test setting and getting volume."""
        new_volume = 1
        mock_instruction.volume = new_volume
        assert mock_instruction.volume == new_volume

    @pytest.mark.parametrize(
        "test_input,expected",
        (
            pytest.param(
                "",
                pytest.raises(InvalidReadInstruction),
                id="Error: Empty Phrase",
            ),
            pytest.param(
                None,
                pytest.raises(InvalidReadInstruction),
                id="Error: None Phrase",
            ),
            pytest.param("optometry", does_not_raise(), id="Normal Phrase"),
        ),
    )
    def test_read(self, mock_instruction, test_input, expected):
        """Test reading a phrase."""
        with expected:
            mock_instruction.phrase = test_input
            mock_instruction.read()

    def test_repr(self, mock_instruction):
        """Test __repr__ method."""
        phrase = "test"
        volume = 50
        rate = 0.5
        voice = 0
        mock_instruction.phrase = phrase
        mock_instruction.volume = volume
        mock_instruction.rate = rate
        mock_instruction.voice = voice

    def test_str(self, mock_instruction):
        """Test __str__ method."""
        assert mock_instruction.phrase == str(mock_instruction)
