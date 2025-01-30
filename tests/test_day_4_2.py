import pytest
from day_4_2 import remove_ms_char, get_mas, iterate_over

@pytest.fixture
def example_data():
    return [
        "M.S",
        ".A.",
        "M.S"
    ]

@pytest.fixture
def sample_data():
    return [
        ".M.S......",
        "..A..MSMS.",
        ".M.S.MAA..",
        "..A.ASMSM.",
        ".M.S.M....",
        "..........",
        "S.S.S.S.S.",
        ".A.A.A.A..",
        "M.M.M.M.M.",
        ".........."
    ]

def test_remove_ms_char():
    assert remove_ms_char('MS') == True
    assert remove_ms_char('MX') == False

def test_get_mas(example_data):
    assert get_mas(1, 1, example_data) == True

def test_iterate_over(example_data, sample_data):
    assert iterate_over(example_data) == 1
    assert iterate_over(sample_data) == 9
