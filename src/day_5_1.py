from functools import cmp_to_key

def comparator(ordering_map: dict) -> callable:
    def closure(a: int, b: int) -> int:
        if a not in ordering_map:
            return 1
        if b in ordering_map[a]:
            return -1
        if b not in ordering_map[a]:
            return 1
        
    return closure

def get_ordering_map_from(page_ordering_rules: list[tuple[int, int]]) -> dict[int, list]:
    ordering_map = dict()
    for x, y in page_ordering_rules:
        if x not in ordering_map:
            ordering_map[x] = [y]
        else:
            ordering_map[x].append(y)

    return ordering_map

def order_pages(pages: list[int], comparator_fn: callable) -> None:
    return sorted(pages, key=cmp_to_key(comparator_fn))

def print_queue(page_rules: list[tuple], manuals: list[list]) -> int:
    ordering_map = get_ordering_map_from(page_rules)
    comparator_fn = comparator(ordering_map)
    sorted_manuals = (
        order_pages(manual, comparator_fn)
        for manual in manuals
        if order_pages(manual, comparator_fn) == manual)
    
    middle_values = (manual[len(manual) // 2] for manual in sorted_manuals)
    return sum(middle_values)
