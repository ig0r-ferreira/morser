import pytest
from typer.testing import CliRunner

from morser.cli import app

from .conftest import ALPHABET_CASES, DIGIT_CASES, PUNCTUATION_CASES

runner = CliRunner()

CHARACTERS_CASES = ALPHABET_CASES + DIGIT_CASES + PUNCTUATION_CASES


@pytest.mark.parametrize('char, expected_result', CHARACTERS_CASES)
def test_encode_command_should_display_the_result(
    char: str, expected_result: str
) -> None:
    result = runner.invoke(app, ['encode', char])

    assert result.exit_code == 0
    assert result.stdout == f'{expected_result}\n'


@pytest.mark.parametrize(
    'morse_code, expected_result',
    ((morse_code, char) for char, morse_code in CHARACTERS_CASES),
)
def test_decode_command_should_display_the_result(
    morse_code: str, expected_result: str
) -> None:
    result = runner.invoke(app, ['decode', '--', morse_code])

    assert result.exit_code == 0
    assert result.stdout == f'{expected_result}\n'
