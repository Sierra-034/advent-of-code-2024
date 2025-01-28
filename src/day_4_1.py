
XMAS = 'XMAS'
XMAS_LENGHT = 4

def iterate_over(word_search: list[list]):
    matches = 0
    for i, row in enumerate(word_search):
        for j, _ in enumerate(row):
            matches += search_over(i, j, word_search)
    
    return matches

def search_over(index_i: int, index_j: int, word_search: list[list]):
    switches = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    matches = 0
    for switch in switches:
        counter = 0
        for i, xmas_char in enumerate(XMAS):
            next_row_pos, next_column_pos = index_i + switch[0] * i, index_j + switch[1] * i
            if (is_out_range(next_row_pos, len(word_search))
                    or is_out_range(next_column_pos, len(word_search[0]))
                    or word_search[next_row_pos][next_column_pos] != xmas_char):
                break

            counter += 1
        if counter == XMAS_LENGHT:
            matches += 1
    
    return matches

def is_out_range(next_pos_index: int, delimeter: int) -> bool:
    return next_pos_index < 0 or next_pos_index >= delimeter