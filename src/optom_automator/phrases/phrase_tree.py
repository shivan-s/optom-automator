"""The Phrase Tree."""

from .types import StageType

SEQUENCE = tuple(
    f"Is it clearer with lens {2*i+1}. Or. Lens {2*i+2}. Or about the same."
    for i in range(11)
)

PHRASE_TREE: dict[str, StageType] = {
    "GREETING": ("random", ("Kia ora", "Hello", "Welcome")),
    "HISTORY": (
        "random",
        (
            "How can I help you out today with your eyesight?",
            "So, how is everything getting along with your vision?",
            "Please tell me about your vision.",
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
    "RIGHT_CYLINDER": ("sequence", SEQUENCE),
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
    "LEFT_CYLINDER": ("sequence", SEQUENCE),
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
