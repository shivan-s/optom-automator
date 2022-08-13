"""Contains the instruction class."""

import pyttsx3

from .exceptions import ReaderError


class Reader:
    """Text to speech class wrapper.

    Attributes:
        phrase (str): The phrase to be uttered.
        rate (int): The rate of utterance.
        volume (float): The volumn of utterance.
        voice (int): The voice of utterance.
        voices (list): The voices available to set for utterance.

    Methods:
        read(): Reads out the phrase with settings.
    """

    def __init__(
        self,
        phrase: str = "",
        rate: int = 200,
        volume: float = 1.00,
        voice: int = 0,
    ):
        """Construct the class.

        Args:
            phrase (str): Phrase to be uttered.
            rate (int): Rate defined by pyttsx3.
            volume (float): Volume defined by pyttsx3.
            voice (int): The voice defined by pyttsx3 and the OS.
        """
        self._phrase = phrase
        self._rate = rate
        self._volume = volume
        self._voice = voice

        self._engine = pyttsx3.init()

    @property
    def phrase(self) -> str:
        """Return the phrase.

        Returns:
            (str): The phrase to be uttered.

        Examples:
            >>> instruction.phrase
            "A phrase"
        """
        return self._phrase

    @phrase.setter
    def phrase(self, phrase: str) -> None:
        """Set phrase to be uttered.

        If the phrase is out of range, the property will be set to False.

        Args:
            phrase (int): Phrase index.

        Examples:
            >>> instruction.phrase = "Hello"
            >>> instruction.phrase
            "Hello"
        """
        self._phrase = phrase

    @property
    def rate(self) -> int:
        """Get the rate of utterance.

        Returns:
            int: The rate of the phase.

        Examples:
            >>> instruction.rate
            200
        """
        return self._rate

    @rate.setter
    def rate(self, rate: int) -> None:
        """Set the rate of utterance.

        Args:
            rate (int): The speed of utterance.

        Examples:
            >>> instruction.rate = 50
            >>> instruction.rate
            50
        """
        self._rate = rate

    @property
    def volume(self) -> float:
        """Return the volume setting.

        Returns:
            float: The current volume setting.
        """
        return self._volume

    @volume.setter
    def volume(self, volume: float) -> None:
        """Set the volume.

        Args:
            volume (float): The volume setting. 1.0 being 100% volume.
        """
        self._volume = volume

    @property
    def voices(self) -> list:
        """Return a list of voices depending on the OS.

        Returns:
            list: Voices available.
        """
        return self._engine.getProperty("voices")

    @property
    def voice(self) -> int:
        """Return current voice by index.

        Returns:
            int: The voice by index.
        """
        return self._voice

    @voice.setter
    def voice(self, voice: int) -> None:
        """Set the voice by index.

        If out of index, the voice will be set to the last indexed voice.

        Args:
            voice (int): [TODO:description]
        """
        voice = abs(int(voice))
        self._voice = voice
        if voice > len(self.voices) - 1:
            self._voice = len(self.voices) - 1

    def read(self):
        """Read the stored phrase.

        Raises:
            InvalidReadInstruction: This is raise if the phrase is empty or set
            to None.
        """
        if self.phrase == "" or self.phrase is None:
            raise ReaderError(message="No phrase set.")
        self._engine.say(self.phrase)
        self._engine.setProperty("rate", self.rate)
        self._engine.setProperty("volume", self.volume)
        self._engine.setProperty("voice", self.voices[self.voice].id)
        self._engine.runAndWait()
        self._engine.stop()

    def __repr__(self):
        """Representation of object."""
        cls = self.__class__.__name__
        return f"{cls}(phrase={self.phrase}, rate={self.rate}, volume={self.volume}, voice={self.voice})"

    def __str__(self):
        """Stringfy object."""
        return self._phrase
