"""Automate Optometrist.

Author: Shivan Sivakumaran
Date: 7/07/2022
Version 0.1.0
"""
import pyttsx3
from rich import print

from optom_automation.utils.phrases import PHRASES

idx = 0


class Instruction:
    """Instruction from the optometrist.

    >>> instruction = Instruction()
    >>> instruction.volume = 100
    >>> instruction.read()
    """

    def __init__(
        self,
        phrase: int = 0,
        rate: int = 200,
        volume: float = 1.0,
        voice: int = 0,
    ):
        """Construct the class.

        Args:
            phrase (int): Index for the phrase to be said in instruction object.
            rate (int): Rate defined by pyttsx3.
            volume (float): Volume defined by pyttsx3.
            voice (int): The voice defined by pyttsx3 and the OS.
        """
        self._phrase = phrase
        self._rate = rate
        self._volume = volume
        self._voice = voice

        self._PHRASES = PHRASES
        self._engine = pyttsx3.init()

    @property
    def phrase(self) -> int:
        """Return phrase index and string.

        Returns:
            (int): The phrase index.
        """
        return self._phrase

    @phrase.setter
    def phrase(self, phrase: int) -> None:
        """Set phrase by index.

        Args:
            phrase (int): Phrase index.

        Returns:
            (bool | str): Returns false if the proviuded value is out of index.
        """
        # TODO: set this to false
        if phrase > len(self._PHRASES) - 1:
            self._phrase = False
        self._phrase = phrase

    @property
    def rate(self) -> int:
        return self._rate

    @rate.setter
    def rate(self, rate: int) -> None:
        self._rate = rate

    @property
    def voices(self) -> list:
        return self._engine.getProperty("voices")

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        self._volume = volume

    @property
    def voice(self) -> int:
        return self._voice

    @voice.setter
    def voice(self, voice: int) -> bool | str:
        # TODO: set voice to false or repeat list
        if voice > len(self.voices) - 1:
            return False
        self._voice = voice
        return self.voices[voice]

    def read(self):
        self._engine.say(self._PHRASES[self._phrase])
        self._engine.runAndWait()
        self._engine.stop()


instruction = Instruction()
instruction.read()


def main():
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
                instruction.phrase += 1

            case 2:
                pass
            case 3:
                instruction.phrase = -1
                instruction.read()
                break

        instruction.read()


if __name__ == "__main__":
    main()
