"""Automate Optometrist.

Author: Shivan Sivakumaran
Date: 7/07/2022
Version 0.1.0
"""
import logging

import pyttsx3
from rich.console import Console
from rich.prompt import IntPrompt
from rich.logging import RichHandler

from optom_automation.utils.phrases import PHRASES

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler()],
)
log = logging.getLogger("rich")

console = Console()


class Instruction:
    """Instruction from the optometrist.

    >>> instruction = Instruction("Hello")
    >>> instruction.volume = 100
    >>> instruction.read()
    """

    def __init__(
        self,
        phrase: str,
        rate: int = 200,
        volume: float = 0.75,
        voice: int = 0,
    ):
        """Construct the class.

        Args:
            phrase (int): Index for the phrase to be said in instruction object.
            rate (int): Rate defined by pyttsx3.
            volume (float): Volume defined by pyttsx3.
            voice (int): The voice defined by pyttsx3 and the OS.
        """
        self._engine = pyttsx3.init()
        self._phrase = phrase
        self._rate = rate
        self._volume = volume
        self._voice = voice

    @property
    def phrase(self) -> str:
        """Return phrase index and string.

        Returns:
            (str): The phrase to be uttered.
        """
        return self._phrase

    @phrase.setter
    def phrase(self, phrase: str) -> None:
        """Set phrase by index.

        If the phrase is out of range, the property will be set to False.

        >>> instruction = Instruction()
        >>> instructions.phrase("Hello")


        Args:
            phrase (int): Phrase index.
        """
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
    def voice(self, voice: int) -> None:
        if voice > len(self.voices) - 1:
            self._voice = False
        self._voice = voice

    def read(self):
        self._engine.say(self.phrase)
        self._engine.setProperty("rate", self.rate)
        self._engine.setProperty("volume", self.volume)
        self._engine.setProperty("voice", self.voices[self.voice].id)
        self._engine.runAndWait()
        self._engine.stop()

    def __repr__(self):
        return self._phrase


def main():
    next_phrase = next(p)
    instruction = Instruction(next_phrase)
    instruction.volume = 0.25
    while True:
        with console.status("Reading...", spinner="aesthetic"):
            instruction.read()
        console.rule("Pick an Action")
        console.print(
            f"1. Repeat Phrase: '{instruction.phrase}'", justify="left"
        )
        console.print(f"2. Next Phrase: '{next_phrase}'", justify="left")
        console.print("3. End Test", justify="left")
        choice = IntPrompt.ask(
            choices=["1", "2", "3"],
            default="1",
        )
        match choice:
            case 1:
                pass
            case 2:
                instruction.phrase = next_phrase
                next_phrase = next(p)
            case 3:
                instruction.phrase = "Thank you."
                instruction.read()
                break


if __name__ == "__main__":
    p = iter(PHRASES)
    main()
