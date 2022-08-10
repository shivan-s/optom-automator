"""Testing phrases."""

import pytest
from optom_automation.instruction.phrases import InvalidPhraseTree, Phrases


class TestPhrase:
    """Test Phrase."""

    def test_phrase(self, mock_phrases):
        """Phrase initialises."""
        isinstance(mock_phrases, Phrases)

    def test_phrase_current(self, mock_phrases):
        """Returns current phrase."""
        assert isinstance(mock_phrases.current, str)

    def test_phrase_peek(self, mock_phrases, mock_phrases_tree):
        """Return the peek."""
        assert mock_phrases.peek == list(mock_phrases_tree.keys())[1]

    def test_phrase_next(self, mock_phrases, mock_phrases_tree):
        """Returns next phrase."""
        assert mock_phrases.next() is True
        assert mock_phrases.current == list(mock_phrases_tree.keys())[1]
        assert mock_phrases.next() is False

    def test_phrase_previous(self, mock_phrases, mock_phrases_tree):
        """Returns next phrase."""
        assert mock_phrases.previous() is False
        mock_phrases.next()
        assert mock_phrases.previous() is True
        assert mock_phrases.current == list(mock_phrases_tree.keys())[0]

    def test_phrase_read(self, mock_phrases, mock_phrases_tree):
        """Test of the phrase can be read.

        Tests the random reader and sequence reader.
        """
        # testing random reading
        assert mock_phrases.read_phrase() in list(mock_phrases_tree.values())[0][1]
        mock_phrases.next()
        # testing sequence
        assert mock_phrases.read_phrase() == list(mock_phrases_tree.values())[1][1][0]
        assert mock_phrases.read_phrase() == list(mock_phrases_tree.values())[1][1][1]
        assert mock_phrases.read_phrase() == list(mock_phrases_tree.values())[1][1][0]

    def test_wrong_stage_type(self):
        """Wrong stage type is set."""
        wrong_stage = Phrases({"Stage0": ("Wrong", ("A", "B"))})
        with pytest.raises(InvalidPhraseTree):
            wrong_stage.read_phrase()

    def test_phrase_len(self, mock_phrases, mock_phrases_tree):
        """Test __len__ magic method."""
        assert len(mock_phrases) == len(mock_phrases_tree.keys())

    def test_phrase_repr(self, mock_phrases):
        """Test __repr__ magic method."""
        assert repr(mock_phrases) == "phrase_object"

    def test_phrase_str(self, mock_phrases):
        """Test __str__ magic method."""
        assert isinstance(str(mock_phrases), str)
