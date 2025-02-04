import pytest
from functools import cmp_to_key
from day_5_1 import comparator, get_ordering_map_from, print_queue

@pytest.fixture
def dummy_manuals():
    return [
        [75,47,61,53,29],
        [97,61,53,29,13],
        [75,29,13],
    ]

@pytest.fixture
def dummy_input_tuple():
    return [(47, 53), (97, 13), (97, 61), (97, 47), (47, 13)]

@pytest.fixture
def dummy_ordering_dict():
    return {47: [53, 13, 61, 29], 97: [13, 61, 47], 75: [29, 53, 47]}

@pytest.fixture
def sample_page_rules():
    return [
        (47,53),
        (97,13),
        (97,61),
        (97,47),
        (75,29),
        (61,13),
        (75,53),
        (29,13),
        (97,29),
        (53,29),
        (61,53),
        (97,53),
        (61,29),
        (47,13),
        (75,47),
        (97,75),
        (47,61),
        (75,61),
        (47,29),
        (75,13),
        (53,13),
    ]

@pytest.fixture
def sample_ordering_dict(sample_page_rules):
    return get_ordering_map_from(sample_page_rules)

@pytest.fixture
def sample_manuals():
    return [
        [75,47,61,53,29],
        [97,61,53,29,13],
        [75,29,13],
        [75,97,47,61,53],
        [61,13,29],
        [97,13,75,29,47],
    ]

def test_comparator_closure(dummy_ordering_dict, sample_ordering_dict):
    comparator_function = comparator(dummy_ordering_dict)
    assert comparator_function(47, 13) == -1

    comparator_function = comparator(sample_ordering_dict)
    assert comparator_function(97, 13) == -1
    assert comparator_function(13, 97) == 1

def test_list_sort(dummy_ordering_dict, sample_ordering_dict):
    comparator_function = comparator(dummy_ordering_dict)
    assert sorted([13, 47], key=cmp_to_key(comparator_function)) == [47, 13]
    assert sorted([47, 97], key=cmp_to_key(comparator_function)) == [97, 47]
    assert sorted([100,300,200], key=cmp_to_key(comparator_function)) == [100,300,200]

    comparator_function = comparator(sample_ordering_dict)
    assert sorted([75,47,61,53,29], key=cmp_to_key(comparator_function)) == [75,47,61,53,29]
    assert sorted([75,97,47,61,53], key=cmp_to_key(comparator_function)) == [97,75,47,61,53]
    assert sorted([61,13,29], key=cmp_to_key(comparator_function)) == [61,29,13]
    assert sorted([97,13,75,29,47], key=cmp_to_key(comparator_function)) == [97,75,47,29,13]

def test_get_ordering_map_from(dummy_input_tuple):
    assert get_ordering_map_from(dummy_input_tuple) == {47: [53, 13], 97: [13, 61, 47]}

def test_print_queue(sample_page_rules, sample_manuals):
    assert print_queue(sample_page_rules, sample_manuals) == 143
