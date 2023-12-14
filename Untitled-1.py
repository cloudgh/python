import random

with open("random_numbers.txt", "w") as file:
    for _ in range(100000):
        file.write(str(random.randint(1, 1000000)) + "\n")


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

with open("random_numbers.txt", "r") as file:
    data = [int(line.strip()) for line in file]

target_element = random.choice(data)


sorted_data = sorted(data)
binary_result = binary_search(sorted_data, target_element)
print(f"Binary Search: Element {target_element} found at index {binary_result}")
