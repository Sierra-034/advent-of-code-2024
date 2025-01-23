import pytest
from day_2_2 import check_if_removing

def test_check_if_removing():
    single_report = [8, 6, 4, 4, 1]
    assert check_if_removing(single_report) == True

@pytest.mark.skip
def test_red_nosed_reports():
    assert False
