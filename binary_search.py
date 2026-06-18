def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value_found = 23
target_value_not_found = 100

print(binary_search(sorted_array, target_value_found))
print(binary_search(sorted_array, target_value_not_found))