import pytest
from roman_numerals import RomanNumerals

#deklarujemy metodę taką samą jak argument:
@pytest.fixture
def roman():
    roman = RomanNumerals()
    return roman


def test_initial(roman):
    assert roman

@pytest.mark.parametrize("nr, expected", (
                        (3, 3),
                        (4, 4)
                         ))
def test_rm_input(roman, nr, expected):
    rm = RomanNumerals(nr)
    assert expected == rm.input()
