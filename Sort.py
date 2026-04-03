import time

comparisons = 0
swaps = 0

def reset_counters():
    global comparisons, swaps
    comparisons = 0
    swaps = 0

def merge_sort(arr, depth=0):
    global comparisons
    print("  " * depth + f"Split: {arr}")

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    return merge(left, right, depth)

def merge(left, right, depth):
    global comparisons
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    print("  " * depth + f"Merge: {result}")
    return result

def quick_sort(arr, depth=0):
    global comparisons, swaps
    print("  " * depth + f"QS: {arr}")

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left, middle, right = [], [], []

    for x in arr:
        comparisons += 1
        if x < pivot:
            left.append(x)
            swaps += 1
        elif x > pivot:
            right.append(x)
            swaps += 1
        else:
            middle.append(x)

    return quick_sort(left, depth+1) + middle + quick_sort(right, depth+1)

def linear_search(arr, target):
    global comparisons
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    global comparisons
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [5, 2, 9, 1, 5, 6]

print("\nMERGE SORT")
reset_counters()
start = time.time()
sorted_arr = merge_sort(arr)
end = time.time()
print("Sorted:", sorted_arr)
print("Comparisons:", comparisons, "Time:", end - start)

print("\nQUICK SORT")
reset_counters()
start = time.time()
sorted_arr = quick_sort(arr)
end = time.time()
print("Sorted:", sorted_arr)
print("Comparisons:", comparisons, "Swaps:", swaps, "Time:", end - start)

print("\nSEARCH")
reset_counters()
print("Linear Search:", linear_search(sorted_arr, 5))
print("Comparisons:", comparisons)

reset_counters()
print("Binary Search:", binary_search(sorted_arr, 5))
print("Comparisons:", comparisons)
