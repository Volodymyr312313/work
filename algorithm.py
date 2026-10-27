# Стек і черга від більшого значення час обробки буле більшим тобто O(n)
arr = list(range(0, 100000000, 5)) # list = O(n)

def linear_search(arr, target):
    for num, value in enumerate(arr):
        if value == target:
            return num  
    return -1

print(linear_search(arr, 10000000))  


def binary_search(arr, target): # O log(n)
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1

print(binary_search(arr, 10000000))  
