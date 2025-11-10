def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


user_input = input("Enter numbers separated by space: ").strip()
arr = [int(x) for x in user_input.split()]
print("Original array:", arr)

selection_sort(arr)
print("Sorted array:  ", arr)
