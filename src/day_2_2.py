from common import prepare_day02_input_data
from day_2_1 import IncreasingSafeChecker, DecreasingSafeChecker, ReportChecker, \
    check_all_increasing_safe, check_all_decreasing_safe, red_nosed_reports

class RemovingChecker(ReportChecker):
    def check(self, report):
        if check_if_removing(report):
            return True
        return super().check(report)

def check_if_removing(report: list):
    aux_report = report.copy()
    index = 0
    while index < len(report):
        del aux_report[index]
        if check_all_increasing_safe(aux_report) or check_all_decreasing_safe(aux_report):
            return True
        aux_report = report.copy()
        index += 1

    return False

def red_nosed_reports(report_list: list) -> int:
    safe_reports = 0
    for report in report_list:
        if (check_all_increasing_safe(report) 
            or check_all_decreasing_safe(report)
            or check_if_removing(report)):
            safe_reports += 1
    
    return safe_reports

def main():
    report_list = prepare_day02_input_data()
    print(red_nosed_reports(report_list))

if __name__ == '__main__':
    main()
