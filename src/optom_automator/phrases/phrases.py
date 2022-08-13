"""Phrases module."""

import random

from .exceptions import PhrasesError
from .phrase_tree import PHRASE_TREE
from .types import StageType


class Phrases:
    """Interface to allow phrase tree to be access.

    Attributes:
        current (str): The current stage.
        peek (str): Provides the next stage.

    Methods:
        read_phrase(): Reads phrase from stage.
        next(): Moves to the next stage.
    """

    def __init__(self, phrase_tree: dict[str, StageType] = PHRASE_TREE):
        """Construct Phrases object.

        Args:
            phrase_tree (dict[str, StageType]): This is the phrase tree,
            containing all dialogue.
        """
        self._current = 0
        self._phrase_tree = phrase_tree
        self._stages = list(phrase_tree.keys())
        self._sequence = 0

    @property
    def current(self) -> str:
        """Provide current stage. And not a index.

        Returns:
            str: The current stage.

        Examples:
            >>> phrase.current_phrase
            >>> "This is the current phrase"
        """
        return self._stages[self._current]

    @property
    def peek(self) -> str | None:
        """Return the next stage by peeking.

        If the current stage is the last stage. Then `None` is returned.

        Returns:
            str | None: The next phrase. Or False if there are no more phrases.

        Examples:
        >>> phrase.peek
        "The next phrase"

        # example when current phrase is last
        >>> phrase.peek
        None
        """
        next_idx = self._current + 1
        if next_idx > len(self._stages) - 1:
            return None
        return self._stages[next_idx]

    def _reset_sequence(self, default: int = 0):
        self._sequence = default

    def next(self) -> bool:
        """Move to next stage.

        Returns:
            bool: To confirm if the move took place. `True` if it moved to next
            stage and `False` if it did not (i.e. at last stage).

        Examples:
            >>> phrase.read_phrase()
            "Current phrase."
            >>> phrase.next()
            True
            >>> phrase.read_phrase()
            "Next and final pharse."
            >>> phrase.next()
            False
        """
        if self.peek is None:
            return False
        self._reset_sequence()
        self._current += 1
        return True

    def previous(self) -> bool:
        """Move to previous stage.

        Returns:
            bool: To confirm is moved to previous stage. `True` if successful,
            and `False` is not (i.e. at first stage).

        Examples:
            >>> phrase.read_phrase()
            "2nd phrase."
            >>> phrase.previous()
            True
            >>> phrase.read_phrase()
            "1st phrase."
            >>> phrase.previous()
            False
        """
        if self._current > 0:
            self._reset_sequence()
            self._current -= 1
            return True
        return False

    def _read_random(self, phrases):
        phrases = self._phrase_tree[self.current][1]
        return random.choice(phrases)

    def _read_sequence(self, phrases):
        phrase = phrases[self._sequence]
        self._sequence += 1
        if self._sequence > len(phrases) - 1:
            self._reset_sequence()
        return phrase

    def read_phrase(self) -> str:
        """Read the phrase according to the stage.

        Returns:
            str: The phrase.

        Examples:
        >>> phrase.read_phrase()
        "Reading phrase"
        """
        stage = self._phrase_tree[self.current]
        match stage[0]:
            case "random":
                phrase = self._read_random(stage[1])
            case "sequence":
                phrase = self._read_sequence(stage[1])
            case _:
                raise PhrasesError(
                    value=stage[0],
                    message="The stage types can only be set to 'random' and 'sequence'.",
                )
        return phrase

    def __len__(self) -> int:
        """Return number of phrases.

        Returns:
            int: Number of phrases.
        """
        return len(self._stages)

    def __repr__(self) -> str:
        """Representation of the object.

        Returns:
            str: The object representation.
        """
        return "phrase_object"

    def __str__(self) -> str:
        """Call string of object.

        Returns:
            str: The phrase the object is set to. As well as the index and
            total size.
        """
        return (
            f"({self._current}/{len(self._phrase_tree)}): {self._stages[self._current]}"
        )
