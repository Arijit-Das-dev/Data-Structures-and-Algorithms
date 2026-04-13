def selection_sort(arr):
    
    n = len(arr)

    for i in range(0, n):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:

                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

nums = [5, 7, 8, 4, 1, 6, 9, 2]
print(selection_sort(nums))