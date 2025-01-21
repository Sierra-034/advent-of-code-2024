from heapq import heappush

def read_stdin_lines():
    try:
        while True:
            line = input()
            if not line: break
            yield line
    except EOFError:
        return
        
def prepare_day01_input_data():
    left_list = list()
    right_list = list()

    for line in read_stdin_lines():
        left, right = line.split()
        heappush(left_list, int(left))
        heappush(right_list, int(right))
    
    return left_list, right_list

def prepare_day02_input_data():
    report_list = list()

    for line in read_stdin_lines():
        report = list(map(int, line.split()))
        report_list.append(report)
    
    return report_list

def prepare_day03_input_data():
    lines = list()
    for line in read_stdin_lines():
        lines.append(line)
    return lines
