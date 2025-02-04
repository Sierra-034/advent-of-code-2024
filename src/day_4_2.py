from common import prepare_day04_input_data


def ceres_search(input_matrix: list[str]) -> int:
    mas_counter = 0
    for apos in get_apos_from(input_matrix):
        if is_mas(*apos, input_matrix):
            mas_counter += 1
    
    return mas_counter

def get_apos_from(input_matrix: list[str]):
    for index_i, element_i in enumerate(input_matrix):
        for index_j, element_j in enumerate(element_i):
            if element_j == 'A':
                yield index_i, index_j

def is_mas(index_a: int, index_b: int, input_matrix: list[str]) -> bool:
    if (is_out_range(index_a, len(input_matrix))
        or is_out_range(index_b, len(input_matrix[0]))):
        return False
    
    counter = 0
    around_chars = get_around_chars(index_a, index_b, input_matrix)
    for element in around_chars:
        if remove_ms_char(element):
            counter += 1
    
    return counter == 2

def get_around_chars(index_a: int, index_b: int, input_matrix: list[str]) -> list[str]:
    ms_chars = list()
    ms_chars.append(
        str(input_matrix[index_a - 1][index_b - 1]
            + input_matrix[index_a + 1][index_b + 1]))
    ms_chars.append(
        str(input_matrix[index_a - 1][index_b + 1]
            + input_matrix[index_a + 1][index_b - 1]))
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
    print(ceres_search(input_matrix))

if __name__ == '__main__':
    main()
