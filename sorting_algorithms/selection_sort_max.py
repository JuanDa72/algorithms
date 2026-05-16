def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1, 0, -1):
        max_index = 0

        for j in range(1, i + 1):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


print(selection_sort([64, 25, 12, 22, 11]))