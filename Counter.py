from collections import Counter

def count_elements(input_list):
    element_counter = Counter(input_list)
    
    result_dict = {f'count-{key}': value for key, value in element_counter.items()}
    
    return result_dict

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_elements(my_list)

print(result)
