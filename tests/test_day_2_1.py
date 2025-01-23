import pytest
from day_2_1 import IncreasingSafeChecker, DecreasingSafeChecker, report_iterator, \
    red_nosed_reports


@pytest.fixture
def get_safe_checker():
    return IncreasingSafeChecker(DecreasingSafeChecker())

def test_report_iterator():
    report_list = [1, 2, 3, 4, 5]
    
    iterator = report_iterator(report_list)
    assert next(iterator) == (1, 2)
    assert next(iterator) == (2, 3)
    assert next(iterator) == (3, 4)
    assert next(iterator) == (4, 5)
    with pytest.raises(StopIteration):
        next(iterator)

def test_increasing_safe_checker_class():
    increasing_checker = IncreasingSafeChecker()
    assert increasing_checker.check([1, 2, 3, 5]) == True
    assert increasing_checker.check([1, 2, 3, 3]) == False
    assert increasing_checker.check([1, 2, 3, 6]) == True
    assert increasing_checker.check([1, 2, 3, 7]) == False


def test_sample_data_increasing_safe_checker_class():
    increasing_checker = IncreasingSafeChecker()
    assert increasing_checker.check([7, 6, 4, 2, 1]) == False
    assert increasing_checker.check([1, 2, 7, 8, 9]) == False
    assert increasing_checker.check([9, 7, 6, 2, 1]) == False
    assert increasing_checker.check([1, 3, 2, 4, 5]) == False
    assert increasing_checker.check([8, 6, 4, 4, 1]) == False
    assert increasing_checker.check([1, 3, 6, 7, 9]) == True

def test_decreasing_safe_checker_class():
    decreasing_checker = DecreasingSafeChecker()
    assert decreasing_checker.check([5, 3, 2, 1]) == True
    assert decreasing_checker.check([3, 3, 2, 1]) == False
    assert decreasing_checker.check([6, 3, 2, 1]) == True
    assert decreasing_checker.check([7, 3, 2, 1]) == False

def test_sample_data_decreasing_safe_checker_class():
    decreasing_checker = DecreasingSafeChecker()
    assert decreasing_checker.check([7, 6, 4, 2, 1]) == True
    assert decreasing_checker.check([1, 2, 7, 8, 9]) == False
    assert decreasing_checker.check([9, 7, 6, 2, 1]) == False
    assert decreasing_checker.check([1, 3, 2, 4, 5]) == False
    assert decreasing_checker.check([8, 6, 4, 4, 1]) == False
    assert decreasing_checker.check([1, 3, 6, 7, 9]) == False

def test_red_nosed_reports(get_safe_checker):
    sample_data = [
        [1, 2, 3, 5],
        [1, 2, 3, 3],
        [1, 2, 3, 6],
        [1, 2, 3, 7],
        [6, 3, 2, 1],
        [5, 3, 2, 1]
    ]
    assert red_nosed_reports(sample_data, get_safe_checker) == 4

def test_sample_data_red_nosed_reports(get_safe_checker):
    sample_data = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]
    assert red_nosed_reports(sample_data, get_safe_checker) == 2
