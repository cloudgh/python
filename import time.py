import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def generate_and_sort(size):
    data = [random.randint(1, 1000000) for _ in range(size)]
    with open(f"data_{size}.txt", "w") as file:
        file.write("\n".join(map(str, data)))

    with open(f"data_{size}.txt", "r") as file:
        data = [int(line.strip()) for line in file]

        start_time = time.time()
        
        finish_time = time.time()

        print(f"Size: {size}, Time: {finish_time - start_time} seconds")

sizes = [100, 1000, 10000, 100000, 1000000]

for size in sizes:
    generate_and_sort(size)
