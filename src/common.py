
def read_stdin_lines():
    try:
        while True:
            line = input()
            yield line
    except EOFError:
        return
        
def prepare_day01_input_data():
    left_list = list()
    right_list = list()

    for line in read_stdin_lines():
        if not line:
            break
        
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
    
    return left_list, right_list

def prepare_day02_input_data():
    report_list = list()

    for line in read_stdin_lines():
        if not line:
            break
        
        report = list(map(int, line.split()))
        report_list.append(report)
    
    return report_list
