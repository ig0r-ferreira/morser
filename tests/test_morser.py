import pytest

from morser import decode_morse_code, encode_text_to_morse_code

from .conftest import ALPHABET_CASES, DIGIT_CASES, PUNCTUATION_CASES


def test_encode_empty_string_should_return_an_error() -> None:
    with pytest.raises(
        ValueError, match="Parameter 'plain_text' is an empty string."
    ):
        encode_text_to_morse_code(' ')


def test_encode_string_with_more_than_one_space_between_words() -> None:
    result = encode_text_to_morse_code('HELLO                 WORLD')
    assert result == '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'


@pytest.mark.parametrize('letter, expected_output', ALPHABET_CASES)
def test_encode_alphabet(letter: str, expected_output: str) -> None:
    result = encode_text_to_morse_code(letter)
    assert result == expected_output


@pytest.mark.parametrize('digit, expected_output', DIGIT_CASES)
def test_encode_digits(digit: str, expected_output: str) -> None:
    result = encode_text_to_morse_code(digit)
    assert result == expected_output


@pytest.mark.parametrize('punctuation, expected_output', PUNCTUATION_CASES)
def test_encode_punctuation(punctuation: str, expected_output: str) -> None:
    result = encode_text_to_morse_code(punctuation)
    assert result == expected_output


def test_encode_a_sentence() -> None:
    result = encode_text_to_morse_code('Programming is cool.')
    assert (
        result
        == '.--. .-. --- --. .-. .- -- -- .. -. --.   .. ...   -.-. --- --- .-.. .-.-.-'
    )


def test_decode_empty_string_should_return_an_error() -> None:
    with pytest.raises(
        ValueError, match="Parameter 'morse_code' is an empty string."
    ):
        decode_morse_code(' ')


def test_decode_morse_code_with_invalid_spaces_should_return_an_error() -> None:
    with pytest.raises(
        ValueError, match='Morse code contains invalid spaces.'
    ):
        decode_morse_code('.... . .-.. .-.. ---      .-- --- .-. .-.. -..')


def test_decode_morse_code_with_invalid_characters() -> None:
    with pytest.raises(
        ValueError, match='Morse code contains invalid characters.'
    ):
        decode_morse_code('.... . .-.. .-.. @   .-- --- .-. .-.. -..')


def test_encode_and_decode_a_text() -> None:
    text = (
        'Lorem Ipsum is simply dummy text of the printing and typesetting '
        "industry. Lorem Ipsum has been the industry's standard dummy text ever "
        'since the 1500s, when an unknown printer took a galley of type and '
        'scrambled it to make a type specimen book. It has survived not only five '
        'centuries, but also the leap into electronic typesetting, remaining '
        'essentially unchanged. It was popularised in the 1960s with the release '
        'of Letraset sheets containing Lorem Ipsum passages, and more recently '
        'with desktop publishing software like Aldus PageMaker including versions '
        'of Lorem Ipsum.'
    )
    result = encode_text_to_morse_code(text)
    assert decode_morse_code(result) == text.upper()
