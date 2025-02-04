import pytest
from day_4_2 import remove_ms_char, is_mas, ceres_search, get_apos_from

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

def test_get_mas(example_data, sample_data):
    assert is_mas(1, 1, example_data) == True
    assert is_mas(2, 6, sample_data) == True
    assert is_mas(2, 1, sample_data) == False


def test_ceres_search(example_data, sample_data):
    assert ceres_search(example_data) == 1
    assert ceres_search(sample_data) == 9

def test_get_apos(example_data):
    iterator = iter(get_apos_from(example_data))
    assert next(iterator) == (1, 1)
    with pytest.raises(StopIteration):
        next(iterator)
