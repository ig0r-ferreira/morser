import pytest

from morser import encode


def test_encode_empty_string_should_return_an_error() -> None:
    with pytest.raises(
        ValueError, match="Parameter 'plain_text' is an empty string."
    ):
        encode(' ')


def test_encode_string_with_more_than_one_space_between_words() -> None:
    result = encode('HELLO                 WORLD')
    assert result == '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'


@pytest.mark.parametrize(
    'letter, expected_output',
    [
        ('A', '.-'),
        ('B', '-...'),
        ('C', '-.-.'),
        ('D', '-..'),
        ('E', '.'),
        ('F', '..-.'),
        ('G', '--.'),
        ('H', '....'),
        ('I', '..'),
        ('J', '.---'),
        ('K', '-.-'),
        ('L', '.-..'),
        ('M', '--'),
        ('N', '-.'),
        ('O', '---'),
        ('P', '.--.'),
        ('Q', '--.-'),
        ('R', '.-.'),
        ('S', '...'),
        ('T', '-'),
        ('U', '..-'),
        ('V', '...-'),
        ('W', '.--'),
        ('X', '-..-'),
        ('Y', '-.--'),
        ('Z', '--..'),
    ],
)
def test_encode_alphabet(letter: str, expected_output: str) -> None:
    result = encode(letter)
    assert result == expected_output


@pytest.mark.parametrize(
    'number, expected_output',
    [
        ('0', '-----'),
        ('1', '.----'),
        ('2', '..---'),
        ('3', '...--'),
        ('4', '....-'),
        ('5', '.....'),
        ('6', '-....'),
        ('7', '--...'),
        ('8', '---..'),
        ('9', '----.'),
    ],
)
def test_encode_numbers(number: str, expected_output: str) -> None:
    result = encode(number)
    assert result == expected_output


@pytest.mark.parametrize(
    'punctuation, expected_output',
    [
        ('.', '.-.-.-'),
        (',', '--..--'),
        ('?', '..--..'),
        ("'", '.----.'),
        ('!', '-.-.--.'),
        ('/', '-..-.'),
        ('(', '-.--.'),
        (')', '-.--.-'),
        ('&', '.-...'),
        (':', '---...'),
        (';', '-.-.-.'),
        ('=', '-...-'),
        ('+', '.-.-.'),
        ('-', '-....-'),
        ('_', '..--.-'),
        ('"', '.-..-.'),
        ('$', '...-..-'),
        ('@', '.--.-.'),
    ],
)
def test_encode_punctuation(punctuation: str, expected_output: str) -> None:
    result = encode(punctuation)
    assert result == expected_output


def test_encode_a_sentence() -> None:
    result = encode('Programming is cool.')
    assert (
        result
        == '.--. .-. --- --. .-. .- -- -- .. -. --.   .. ...   -.-. --- --- .-.. .-.-.-'
    )
