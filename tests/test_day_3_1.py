import pytest
from day_3_1 import get_matches, mull_it_over

@pytest.fixture
def input_lines():
    return ['xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))']

def test_get_matches(input_lines):
    line = input_lines
    matches = get_matches(line[0])
    assert len(matches) == 4

def test_mull_it_over(input_lines):
    lines = input_lines
    assert mull_it_over(lines) == 161
