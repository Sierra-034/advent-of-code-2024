from common import prepare_day04_input_data


def iterate_over(input_matrix: list[str]) -> int:
    counter = 0
    for index_i, element_i in enumerate(input_matrix):
        for index_j, element_j in enumerate(element_i):
            if element_j == 'A' and get_mas(index_i, index_j, input_matrix):
                counter += 1
    
    return counter

def get_mas(index_a: int, index_b: int, input_matrix: list[str]) -> int:
    if is_out_range(index_a, len(input_matrix)) or is_out_range(index_b, len(input_matrix[0])):
        return False
    
    around_pos = get_around_pos(index_a, index_b)
    characters = get_around_chars(around_pos, input_matrix)
    counter = 0
    for element in characters:
        if remove_ms_char(element):
            counter += 1
    
    return counter == 2

def get_around_pos(index_a: int, index_b: int) -> list[tuple]:
    return [(index_a - 1, index_b - 1), (index_a + 1, index_b + 1),
            (index_a - 1, index_b + 1), (index_a + 1, index_b - 1)]

def get_around_chars(around_positions: list[tuple], input_matrix: list[str]) -> list[str]:
    ms_chars = list()
    ms_chars.append(
        str(input_matrix[around_positions[0][0]][around_positions[0][1]]
            + input_matrix[around_positions[1][0]][around_positions[1][1]]))
    ms_chars.append(
        str(input_matrix[around_positions[2][0]][around_positions[2][1]]
            + input_matrix[around_positions[3][0]][around_positions[3][1]]))
    return ms_chars

def is_out_range(index: int, delimeter: int) -> bool:
    return index - 1 < 0 or index + 1 >= delimeter

def remove_ms_char(characters: str) -> bool:
    ms_str = 'MS'
    for character in characters:
        ms_str = ms_str.replace(character, '')

    return len(ms_str) == 0

def main():
    input_matrix = prepare_day04_input_data()
    print(iterate_over(input_matrix))

if __name__ == '__main__':
    main()

