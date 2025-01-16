import pytest
from day_1_2 import get_frequency_dict, get_similarity_score

def test_get_frequency_dict():
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    frequency_dict = get_frequency_dict(left_list, right_list)
    assert frequency_dict == {3: 3, 4: 1, 2: 0, 1: 0}

def test_get_similarity_socore():
    frequency_dict = {3: 3, 4: 1, 2: 0, 1: 0}
    left_list = [3, 4, 2, 1, 3, 3]

    similarity_score = get_similarity_score(frequency_dict, left_list)
    assert similarity_score == 31
