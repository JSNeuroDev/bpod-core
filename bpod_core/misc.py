"""Miscellaneous tools that don't fit the other categories."""

import difflib
import re

RE_SNAKE_CASE = re.compile(r'(?<=[a-z])(?=[A-Z\d])')
RE_UNDERSCORES = re.compile(r'_{2,}')


def convert_to_snake_case(input_str: str) -> str:
    """
    Convert a given string to snake_case.

    This function replaces spaces with underscores and inserts underscores
    between lowercase and uppercase letters to convert a string to snake_case.

    Parameters
    ----------
    input_str : str
        The input string to be converted.

    Returns
    -------
    str
        The converted snake_case string.
    """
    input_str = input_str.replace(' ', '_')
    snake_case_str = re.sub(RE_SNAKE_CASE, '_', input_str)
    snake_case_str = re.sub(RE_UNDERSCORES, '_', snake_case_str)
    return snake_case_str.lower()


def suggest_similar(
    invalid_string: str,
    valid_strings: list[str],
    format_string: str = " - did you mean '{}'?",
    cutoff: float = 0.6,
) -> str:
    """
    Suggest a similar valid string based on the given invalid string.

    This function uses a similarity matching algorithm to find the closest match from a
    list of valid strings. If a match is found above the specified cutoff, it returns a
    formatted suggestion string.

    Parameters
    ----------
    invalid_string : str
        The string that is invalid or misspelled.
    valid_strings : list[str]
        A list of valid strings to compare against.
    format_string : str, optional
        The format string for the suggestion. Defaults to " - did you mean '{}'?".
    cutoff : float, optional
        The similarity threshold for considering a match. Defaults to 0.6.

    Returns
    -------
    str
        A formatted suggestion string if a match is found, otherwise an empty string.
    """
    matches = difflib.get_close_matches(invalid_string, valid_strings, 1, cutoff)
    return format_string.format(matches[0]) if len(matches) > 0 else ''
