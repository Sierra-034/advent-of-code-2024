
def read_stdin_lines():
    try:
        while True:
            line = input()
            yield line
    except EOFError:
        return
