def largestNumber(arr):

    max_number = arr[0]
    
    n = len(arr)

    for i in range(1, n):

        if arr[i] > max_number:
            max_number = arr[i]

    return max_number

nums = [55, 32, -97, 99, 3, 67]

print(largestNumber(nums))