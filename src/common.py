
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
