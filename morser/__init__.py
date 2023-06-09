import re

from .dictionary import ENCODE_TABLE


def _format_spaces_between_words(text: str) -> str:
    return re.sub(r'\s{1,}', ' ', text.strip())


def encode(plain_text: str) -> str:
    if plain_text.isspace():
        raise ValueError("Parameter 'plain_text' is an empty string.")

    return ' '.join(
        ENCODE_TABLE.get(char, '#')
        for char in _format_spaces_between_words(plain_text).upper()
    )
