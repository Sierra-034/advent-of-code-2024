from re import finditer
from common import prepare_day03_input_data

def get_matches(line: str) -> list:
    matches = list()
    for match in finditer(r"mul\((?P<factor_1>[0-9]{1,3}),(?P<factor_2>[0-9]{1,3})\)", line):
        matches.append(match)
    
    return matches

def get_product(match) -> int:
    factor_1 = int(match.group("factor_1"))
    factor_2 = int(match.group("factor_2"))
    return factor_1 * factor_2

def mull_it_over(lines: list) -> int:
    matches = list()
    for line in lines:
        matches += get_matches(line)
    
    product_sum = 0
    for match in matches:
        product_sum += get_product(match)

    return product_sum

def main():
    lines = prepare_day03_input_data()
    print(mull_it_over(lines))

if __name__ == "__main__":
    main()
