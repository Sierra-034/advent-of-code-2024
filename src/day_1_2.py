from common import prepare_day01_input_data

def get_frequency_dict(left_list: list, right_list: list) -> dict:
    frequency_dict = dict()
    for left_element in left_list:
        if left_element not in frequency_dict:
            frequency_dict[left_element] = 0
        else:
            continue

        for right_element in right_list:
            if left_element == right_element:
                frequency_dict[left_element] += 1
        
    return frequency_dict

def get_similarity_socore(frequency_dict: dict, left_list: list) -> int:
    scores = list()
    for left_element in left_list:
        scores.append(left_element * frequency_dict[left_element])
    
    return sum(scores)

if __name__ == '__main__':
    left_list, right_list = prepare_day01_input_data()
    frequency_dict = get_frequency_dict(left_list, right_list)
    similarity_score = get_similarity_socore(frequency_dict, left_list)
    print(similarity_score)
