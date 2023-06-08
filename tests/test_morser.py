import pytest

from morser import encode


@pytest.mark.parametrize(
    'text, expected_result',
    [
        ('Massachusetts', '-- .- ... ... .- -.-. .... ..- ... . - - ...'),
        (
            'Is programming cool?',
            '.. ... / .--. .-. --- --. .-. .- -- -- .. -. --. / '
            '-.-. --- --- .-.. ..--..',
        ),
        (
            'September 13, 2023',
            '... . .--. - . -- -... . .-. / .---- ...-- --..-- / '
            '..--- ----- ..--- ...--',
        ),
        ('Sayōnara', '... .- -.-- # -. .- .-. .-'),
        (
            'Morse code is a method used in telecommunication to encode text '
            'characters as standardized sequences of two different signal '
            'durations, called dots and dashes, or dits and dahs. Morse code '
            'is named after Samuel Morse, one of the inventors of the telegraph.',
            '-- --- .-. ... . / -.-. --- -.. . / .. ... / .- / '
            '-- . - .... --- -.. / ..- ... . -.. / .. -. / '
            '- . .-.. . -.-. --- -- -- ..- -. .. -.-. .- - .. --- -. / - --- / '
            '. -. -.-. --- -.. . / - . -..- - / '
            '-.-. .... .- .-. .- -.-. - . .-. ... / .- ... / '
            '... - .- -. -.. .- .-. -.. .. --.. . -.. / '
            '... . --.- ..- . -. -.-. . ... / --- ..-. / - .-- --- / '
            '-.. .. ..-. ..-. . .-. . -. - / ... .. --. -. .- .-.. / '
            '-.. ..- .-. .- - .. --- -. ... --..-- / -.-. .- .-.. .-.. . -.. '
            '/ -.. --- - ... / .- -. -.. / -.. .- ... .... . ... --..-- / '
            '--- .-. / -.. .. - ... / .- -. -.. / -.. .- .... ... .-.-.- / '
            '-- --- .-. ... . / -.-. --- -.. . / .. ... / -. .- -- . -.. / '
            '.- ..-. - . .-. / ... .- -- ..- . .-.. / -- --- .-. ... . --..-- '
            '/ --- -. . / --- ..-. / - .... . / .. -. ...- . -. - --- .-. ... '
            '/ --- ..-. / - .... . / - . .-.. . --. .-. .- .--. .... .-.-.-',
        ),
    ],
)
def test_encode(text: str, expected_result: str) -> None:
    result = encode(text)
    assert result == expected_result
