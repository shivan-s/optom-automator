"""Automate Optometrist.

Author: Shivan Sivakumaran
Date: 7/07/2022
Version 0.1.0
"""

import pyttsx3

PHRASES = [
    "How can I help you out today with your eyesight?",
    "Please use this device",
    "What is the smallest line that you can read?",
    "Now the other eye.",
    "Is it clearer on the red or green?",
    "Is it better with 1 or 2?",
    "Is the next lens better or worse?",
    "Let's test your other eye",
    "Is it better with 1 or 2?",
]

idx = 0


def read(phrase: str, rate: int = 200, volume: float = 1.0, voice: int = 0):
    """Read."""
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[voice].id)
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    engine.say(phrase)
    engine.runAndWait()
    engine.stop()


read(PHRASES[idx])
while True:
    custom_input = input(
        """
    (1) Next step
    (2) Repeat
    (3) End
        """
    )
    match int(custom_input):
        case 1:
            idx += 1
            if idx > len(PHRASES) - 1:
                read("This concludes the refractive part of the eye test. Thank you.")
                break
        case 2:
            pass
        case 3:
            break

    read(PHRASES[idx])
