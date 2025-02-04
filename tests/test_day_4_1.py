import pytest
from day_4_1 import iterate_over, search_over

@pytest.fixture
def example_word_search():
    return [
        "..X...",
        ".SAMX.",
        ".A..A.",
        "XMAS.S",
        ".X....",
    ]


@pytest.fixture
def word_search_sample():
    return [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]

def test_iterate_over(word_search_sample):
    assert iterate_over(word_search_sample) == 18

def test_iterate_over_example(example_word_search):
    assert iterate_over(example_word_search) == 4

def test_search_over(example_word_search):
    assert search_over(4, 1, example_word_search) == 1
    assert search_over(0, 2, example_word_search) == 1

def test_search_over_sample(word_search_sample):
    assert search_over(5, 6, word_search_sample) == 1
    assert search_over(9, 3, word_search_sample) == 2
