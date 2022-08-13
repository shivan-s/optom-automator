"""Test for instructions."""

from contextlib import nullcontext as does_not_raise

import pytest
from optom_automator.reader import Reader
from optom_automator.reader.exceptions import ReaderError


class TestReader:
    """Tests for Reader."""

    def test_instruction(self, mock_reader):
        """Test if the class can be instantiated."""
        assert isinstance(mock_reader, Reader)

    def test_phrase(self, mock_reader, phrase):
        """Test getting a phrase."""
        assert mock_reader.phrase == phrase

    def test_set_phrase(self, mock_reader):
        """Test setting a phrase."""
        new_phrase = "new phrase"
        mock_reader.phrase = new_phrase
        assert mock_reader.phrase == new_phrase

    def test_get_voices(self, mock_reader):
        """Test retrieving voice."""
        assert isinstance(mock_reader.voices, list)

    def test_voice(self, mock_reader):
        """Test setting and getting voice."""
        len_voices = len(mock_reader.voices)
        # intentionally test outside of range
        new_voice = len_voices + 1
        mock_reader.voice = new_voice
        assert mock_reader.voice == len_voices - 1

    def test_rate(self, mock_reader):
        """Test setting and getting rate."""
        new_rate = 1
        mock_reader.rate = new_rate
        assert mock_reader.rate == new_rate

    def test_volume(self, mock_reader):
        """Test setting and getting volume."""
        new_volume = 1
        mock_reader.volume = new_volume
        assert mock_reader.volume == new_volume

    @pytest.mark.parametrize(
        "test_input,expected",
        (
            pytest.param(
                "",
                pytest.raises(ReaderError),
                id="Error: Empty Phrase",
            ),
            pytest.param(
                None,
                pytest.raises(ReaderError),
                id="Error: None Phrase",
            ),
            pytest.param("optometry", does_not_raise(), id="Normal Phrase"),
        ),
    )
    def test_read(self, mock_reader, test_input, expected):
        """Test reading a phrase."""
        with expected:
            mock_reader.phrase = test_input
            mock_reader.read()

    def test_repr(self, mock_reader):
        """Test __repr__ method."""
        phrase = "test"
        volume = 50
        rate = 0.5
        voice = 0
        mock_reader.phrase = phrase
        mock_reader.volume = volume
        mock_reader.rate = rate
        mock_reader.voice = voice
        assert (
            repr(mock_reader)
            == f"{mock_reader.__class__.__name__}(phrase={phrase}, rate={rate}, volume={volume}, voice={voice})"
        )

    def test_str(self, mock_reader):
        """Test __str__ method."""
        assert mock_reader.phrase == str(mock_reader)
