import pytest
from day_2_1 import report_iterator, check_all_increasing_safe, check_all_decreasing_safe, \
    red_nosed_reports

def test_report_iterator():
    report_list = [1, 2, 3, 4, 5]
    
    iterator = report_iterator(report_list)
    assert next(iterator) == (1, 2)
    assert next(iterator) == (2, 3)
    assert next(iterator) == (3, 4)
    assert next(iterator) == (4, 5)
    with pytest.raises(StopIteration):
        next(iterator)

def test_check_all_increasing_safe():
    assert check_all_increasing_safe([1, 2, 3, 5]) == True
    assert check_all_increasing_safe([1, 2, 3, 3]) == False
    assert check_all_increasing_safe([1, 2, 3, 6]) == True
    assert check_all_increasing_safe([1, 2, 3, 7]) == False

def test_sample_data_check_all_increasing_safe():
    assert check_all_increasing_safe([7, 6, 4, 2, 1]) == False
    assert check_all_increasing_safe([1, 2, 7, 8, 9]) == False
    assert check_all_increasing_safe([9, 7, 6, 2, 1]) == False
    assert check_all_increasing_safe([1, 3, 2, 4, 5]) == False
    assert check_all_increasing_safe([8, 6, 4, 4, 1]) == False
    assert check_all_increasing_safe([1, 3, 6, 7, 9]) == True

def test_check_all_decreasing_safe():
    assert check_all_decreasing_safe([5, 3, 2, 1]) == True
    assert check_all_decreasing_safe([3, 3, 2, 1]) == False
    assert check_all_decreasing_safe([6, 3, 2, 1]) == True
    assert check_all_decreasing_safe([7, 3, 2, 1]) == False

def test_sample_data_check_all_decreasing_safe():
    assert check_all_decreasing_safe([7, 6, 4, 2, 1]) == True
    assert check_all_decreasing_safe([1, 2, 7, 8, 9]) == False
    assert check_all_decreasing_safe([9, 7, 6, 2, 1]) == False
    assert check_all_decreasing_safe([1, 3, 2, 4, 5]) == False
    assert check_all_decreasing_safe([8, 6, 4, 4, 1]) == False
    assert check_all_decreasing_safe([1, 3, 6, 7, 9]) == False

def test_red_nosed_reports():
    sample_data = [
        [1, 2, 3, 5],
        [1, 2, 3, 3],
        [1, 2, 3, 6],
        [1, 2, 3, 7],
        [6, 3, 2, 1],
        [5, 3, 2, 1]
    ]
    assert red_nosed_reports(sample_data) == 4

def test_sample_data_red_nosed_reports():
    sample_data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]
    assert red_nosed_reports(sample_data) == 2
