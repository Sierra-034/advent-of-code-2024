from common import prepare_day02_input_data
from day_2_1 import IncreasingSafeChecker, DecreasingSafeChecker, ReportChecker, \
    red_nosed_reports

class RemovingChecker(ReportChecker):
    def check(self, report):
        aux_report = report.copy()
        index = 0
        increasing_decreasing_checker = IncreasingSafeChecker(DecreasingSafeChecker())
        while index < len(report):
            del aux_report[index]
            if increasing_decreasing_checker.check(aux_report):
                return True
            aux_report = report.copy()
            index += 1

        return super().check(report)

def main():
    report_list = prepare_day02_input_data()
    safe_checker = IncreasingSafeChecker(DecreasingSafeChecker(RemovingChecker()))
    print(red_nosed_reports(report_list, safe_checker))

if __name__ == '__main__':
    main()
