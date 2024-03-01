import random
import timeit

# Реалізація сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Генерація наборів даних різного розміру
sizes = [100, 1000, 10000]
datasets = {size: [random.randint(0, size) for _ in range(size)] for size in sizes}

# Вимірювання часу виконання алгоритмів
execution_times = {"Insertion Sort": [], "Merge Sort": [], "Timsort": []}

for size, data in datasets.items():
    # Копії даних для кожного сортування
    data_for_insertion = data.copy()
    data_for_merge = data.copy()
    data_for_timsort = data.copy()

    # Вимірювання часу для сортування вставками
    insertion_sort_time = timeit.timeit('insertion_sort(data_for_insertion)', globals=globals(), number=1)
    execution_times["Insertion Sort"].append((size, insertion_sort_time))

    # Вимірювання часу для сортування злиттям
    merge_sort_time = timeit.timeit('merge_sort(data_for_merge)', globals=globals(), number=1)
    execution_times["Merge Sort"].append((size, merge_sort_time))

    # Вимірювання часу для Timsort (використовуючи вбудовану функцію sorted)
    timsort_time = timeit.timeit('sorted(data_for_timsort)', globals=globals(), number=1)
    execution_times["Timsort"].append((size, timsort_time))

print(execution_times)

# 'Insertion Sort': [(100, 0.00029150000773370266), (1000, 0.02077520001330413), (10000, 2.3565256999863777)],
# 'Merge Sort': [(100, 0.00021100000594742596), (1000, 0.0025599999935366213), (10000, 0.0343494999979157)],
# 'Timsort': [(100, 1.1099997209385037e-05), (1000, 9.509999654255807e-05), (10000, 0.0012098000152036548)]

