import pytest
from day_2_2 import RemovingChecker

def test_check_if_removing():
    single_report = [8, 6, 4, 4, 1]
    removing_checker = RemovingChecker()
    assert removing_checker.check(single_report) == True

@pytest.mark.skip
def test_red_nosed_reports():
    assert False
