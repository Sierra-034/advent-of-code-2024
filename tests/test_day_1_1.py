import pytest
from day_1_1 import get_total_distance

def test_equal_length_lists():
    assert get_total_distance([1, 2, 3], [4, 5, 6]) == 9
    assert get_total_distance([1, 3, 5], [2, 4, 6]) == 3

def test_unequal_length_lists():
    assert get_total_distance([1, 2], [3, 4, 5]) == 4
    assert get_total_distance([1, 2, 3], [4]) == 3

def test_empty_lists():
    assert get_total_distance([], []) == 0

def test_negative_numbers():
    assert get_total_distance([-1, -2, -3], [-4, -5, -6]) == 9
    assert get_total_distance([-1, -3, -5], [-2, -4, -6]) == 3

def test_sample_data():
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert get_total_distance(left_list, right_list) == 11
