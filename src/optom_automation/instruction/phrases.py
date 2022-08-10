"""Phrases that optometrists use commonly.

How this works?

There is a usual sequence (for refraction). And that is:
    (intro)
    GREETING ->
    HISTORY ->
    (preliminary)
    RIGHT_VA ->
    LEFT_VA ->
    (refraction)
    RIGHT_REDGREEN ->
    RIGHT_CYLINDER ->
    RIGHT_SPHERE ->
    LEFT_SPHERE(R/G) ->
    LEFT_CYLINDER ->
    LEFT_SPHERE(FINE) ->
    (end)
    END_EXAM -|

The capitals represent the "states" of the testing. They can act as keys for
tuples. The tuples provide a little variation in testing.

The tuples phrases can be played in sequence or at random.

This is how the dictionary is constructed roughly:
_PHRASES = {
    "STAGE_1": ("random", ("choice1", "choice2")),
    "STAGE_2": ("sequence", ("choice1", "choice2")),
}
"""

import random
from collections.abc import Iterable

StageType = tuple[str, Iterable[str]]

_PHRASES: dict[str, StageType] = {
    "GREETING": ("random", ("Kia ora", "Hello", "Welcome")),
    "HISTORY": (
        "random",
        (
            "How can I help you out today with your eyesight?",
            "So, how is everything getting along with your vision?",
        ),
    ),
    "RIGHT_VA": (
        "random",
        (
            "Let's take a look at how well you can see. Starting with your right eye, what is the smallest line that you can read?",
        ),
    ),
    "LEFT_VA": (
        "random",
        ("Now with your left eye, what is the smallest line that you can read?",),
    ),
    "RIGHT_REDGREEN": (
        "random",
        (
            "Is it clearer on the red or green side?",
            "Are the symbols clearer on the red or green square?",
        ),
    ),
    "RIGHT_CYLINDER": (
        "sequence",
        (
            "Is it clearer with view 1 or view 2 or about the same?",
            "Is it clearer with lens 3 or lens 4 or about the same?",
            "Is it clearer with lens 5 or lens 6 or about the same?",
            "Is it clearer with lens 7 or lens 8 or about the same?",
            "Is it clearer with lens 9 or lens 10 or about the same?",
        ),
    ),
    "RIGHT_SPHERE": (
        "random",
        ("Is it clearer of worse with the next lens or about the same?",),
    ),
    "LEFT_REDGREEN": (
        "random",
        (
            "Let's do your left eye, is it clearer on the red or green side?",
            "Are the symbols clearer on the red or green square?",
        ),
    ),
    "LEFT_CYLINDER": (
        "sequence",
        (
            "Is it clearer with view 1 or view 2 or about the same?",
            "Is it clearer with lens 3 or lens 4 or about the same?",
            "Is it clearer with lens 5 or lens 6 or about the same?",
            "Is it clearer with lens 7 or lens 8 or about the same?",
            "Is it clearer with lens 9 or lens 10 or about the same?",
        ),
    ),
    "LEFT_SPHERE": (
        "random",
        ("Is it clearer of worse with the next lens or about the same?",),
    ),
    "END_EXAM": (
        "random",
        (
            "You have done well. Thank you.",
            "This concludes the lenses part of the eye exam.",
        ),
    ),
}


class InvalidPhraseTree(Exception):
    """Custom Error for Phrase Trees."""

    def __init__(self, value: str, message: str) -> None:
        """Construct exception."""
        self.value = value
        self.message = message
        super().__init__()


class Phrases:
    """Interface to allow phrase tree to be access.

    Attributes:
        current (str): The current stage.
        peek (str): Provides the next stage.

    Methods:
        read_phrase(): Reads phrase from stage.
        next(): Moves to the next stage.
    """

    def __init__(self, phrase_tree: dict[str, StageType] = _PHRASES):
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
                raise InvalidPhraseTree(
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
