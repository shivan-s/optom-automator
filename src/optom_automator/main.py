"""Optom Automation.

Date: 7/07/2022
"""
from collections.abc import Iterable

from optom_automator.__init__ import __app__, __author__, __version__
from optom_automator.phrases import Phrases
from optom_automator.reader import Reader
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.text import Text
from rich.theme import Theme

reader = Reader()
phrase = Phrases()

custom_theme = Theme(
    {
        "menu_title": "bold cyan",
        "menu_item": "bold magenta",
        "dim": "dim",
        "number": "green",
    }
)
console = Console(theme=custom_theme)


def _detail_element(text: str) -> Text:
    t = Text(text, style="dim")
    t.highlight_regex(r":\s\w+", style="number")
    return t


def _menu_element(text: str) -> Text:
    t = Text(text, style="normal")
    t.highlight_regex(r"\d+\.", style="menu_item")
    t.highlight_regex(r"'\w+'", style="number")
    return t


def _voice_details() -> list[Align]:
    voice_info = reader.voices[reader.voice]
    elements = [
        Align.left(_detail_element(f"\nVoice: {voice_info.name}")),
        Align.left(_detail_element(f"Rate: {reader.rate} words/min")),
    ]
    return elements


def generate_menu(
    choices: Iterable[str | None],
    menu_query: str = "Please choose an option:",
    default_choice: int = 0,
    padding: int = 4,
) -> int:
    """Generate the menu. And also ask for user input.

    Args:
        choices (Iterable[str | None]): Options in the menu.
        menu_query (str): What the question test will be displayed.
        default_choice (int): The default choice as an index.
        padding (int): The padding for the display.

    Returns:
        int: The choice by the user.
    """
    formatted = [
        Align.left(_menu_element(f"{i+1}. {choice}"))
        for i, choice in enumerate(choices)
    ]
    menu_formatted = Align.center(menu_query + "\n", style="menu_title")
    groups = [menu_formatted] + formatted + _voice_details()
    panel = Panel.fit(
        Align.left(Group(*groups)),
        title=f"{__app__} v{__version__}",
        subtitle=f"By {__author__}",
        padding=padding,
    )
    console.clear()
    console.print(panel)
    idx = [str(i + 1) for i, _ in enumerate(choices)]
    choice = IntPrompt.ask(
        choices=idx,
        default=idx[default_choice],
    )
    return int(choice)


def main() -> None:
    """Run main."""
    with console.screen(hide_cursor=False):
        while True:
            with console.status("Reading...", spinner="aesthetic"):
                reader.phrase = phrase.read_phrase()
                reader.read()
            choices = [
                f"Repeat - '{phrase.current}'",
                f"Next - '{phrase.peek}'",
                "Repeat (slower)",
                "Repeat (faster)",
                "Previous",
                "Exit",
            ]
            choice = generate_menu(choices=choices)
            match choice:
                case 1:  # Repeat
                    pass
                case 2:  # Next
                    phrase.next()
                case 3:  # Repeat slower
                    reader.rate -= 50
                case 4:  # Repeat faster
                    reader.rate += 50
                case 5:  # Previous
                    phrase.previous()
                case 6:  # Exit
                    break


if __name__ == "__main__":
    main()
