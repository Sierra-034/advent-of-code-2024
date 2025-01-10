import sys
from io import StringIO
import pytest
from src.common import read_stdin_lines, prepare_day01_input_data, \
    prepare_day02_input_data

def test_read_stdin_lines(monkeypatch):
    input_data = "line1\nline2\nline3\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    expected_lines = ["line1", "line2", "line3"]
    result = list(read_stdin_lines())
    
    assert result == expected_lines

def test_read_stdin_lines_empty(monkeypatch):
    input_data = ""
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    expected_lines = []
    result = list(read_stdin_lines())
    
    assert result == expected_lines

def test_read_stdin_lines_single_line(monkeypatch):
    input_data = "single_line\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    expected_lines = ["single_line"]
    result = list(read_stdin_lines())
    
    assert result == expected_lines

def test_prepare_day01_input_data(monkeypatch):
    input_data = "1 2\n3  4\n5\t6\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    left_list, right_list = prepare_day01_input_data()
    
    assert left_list == [1, 3, 5]
    assert right_list == [2, 4, 6]

def test_prepare_day01_input_data_empty(monkeypatch):
    input_data = ""
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    left_list, right_list = prepare_day01_input_data()
    
    assert left_list == []
    assert right_list == []

def test_prepare_day01_input_data_single_line(monkeypatch):
    input_data = "7 8\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    left_list, right_list = prepare_day01_input_data()
    
    assert left_list == [7]
    assert right_list == [8]

def test_prepare_day02_input_data(monkeypatch):
    input_data = "1 2 3 4\n5 6 7 8\n9 10 11 12\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    report_list = prepare_day02_input_data()
    
    assert report_list == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

def test_prepare_day02_input_data_variable_length(monkeypatch):
    input_data = "1 2 3 4\n5 6 7\n8 9\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    report_list = prepare_day02_input_data()
    
    assert report_list == [[1, 2, 3, 4], [5, 6, 7], [8, 9]]

def test_prepare_day02_input_data_empty(monkeypatch):
    input_data = ""
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    report_list = prepare_day02_input_data()
    
    assert report_list == []

def test_prepare_day02_input_data_single_line(monkeypatch):
    input_data = "1 2 3 4\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    report_list = prepare_day02_input_data()
    
    assert report_list == [[1, 2, 3, 4]]
