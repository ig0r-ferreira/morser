from .dictionary import TRANSLATION_TABLE


def encode(text: str) -> str:
    return ' '.join(TRANSLATION_TABLE.get(char, '#') for char in text.upper())
