"""The Phrase Tree."""

from .types import StageType

PHRASE_TREE: dict[str, StageType] = {
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
