def selectionSort(arr):

    n = len(arr)

    for i in range(0, n):
        max_idx = i

        for j in range(i+1, n):
           if arr[j] > arr[max_idx]:
               
               max_idx = j
    
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr

nums = [5, 7, 8, 4, 1, 6, 9, 2]
print(selectionSort(nums))