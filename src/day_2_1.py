from common import prepare_day02_input_data

class ReportChecker:
    def __init__(self, successor=None):
        self._successor = successor

    def check(self, report):
        if self._successor:
            return self._successor.check(report)
        return False

class IncreasingSafeChecker(ReportChecker):
    def check(self, report):
        for left, right in report_iterator(report):
            safe_diff = right - left
            if safe_diff <= 0 or safe_diff > 3:
                return super().check(report)
        return True

class DecreasingSafeChecker(ReportChecker):
    def check(self, report):
        for left, right in report_iterator(report):
            safe_diff = right - left
            if safe_diff >= 0 or safe_diff < -3:
                return super().check(report)
        return True

def report_iterator(report_list: list):
    pointer = 1
    while pointer < len(report_list):
        yield report_list[pointer - 1], report_list[pointer]
        pointer += 1

def check_all_increasing_safe(report_list: list) -> bool:
    for left, right in report_iterator(report_list):
        safe_diff = right - left
        if safe_diff <= 0 or safe_diff > 3:
            return False
    return True

def check_all_decreasing_safe(report_list: list) -> bool:
    for left, right in report_iterator(report_list):
        safe_diff = right - left
        if safe_diff >= 0 or safe_diff < -3:
            return False
    return True

def red_nosed_reports(report_list: list) -> int:
    safe_reports = 0
    for report in report_list:
        if check_all_increasing_safe(report) or check_all_decreasing_safe(report):
            safe_reports += 1
    
    return safe_reports

def main():
    report_list = prepare_day02_input_data()
    print(red_nosed_reports(report_list))

if __name__ == "__main__":
    main()
