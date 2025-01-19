from heapq import heappop
from common import prepare_day01_input_data

def get_total_distance(left_list: list, right_list: list) -> int:
    sum = 0
    while left_list and right_list:
        left, right = heappop(left_list), heappop(right_list)
        sum += abs(left - right)
    
    return sum

if __name__ == "__main__":
    left_list, right_list = prepare_day01_input_data()
    total_distance = get_total_distance(left_list, right_list)
    print(total_distance)
