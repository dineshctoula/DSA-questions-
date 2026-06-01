# Question: Find the second largest (or second last in sorted order) element in an array.

# Approach 1: Sorting (Simple but has drawbacks)
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sort implementation
# Drawback: If the array has duplicates of the maximum element (e.g., [10, 10, 8]), 
# this will incorrectly return 10 instead of 8.
def second_largest_sorting(arr):
    if len(arr) < 2:
        return None
    sorted_arr = sorted(list(set(arr))) # Remove duplicates first and sort
    if len(sorted_arr) < 2:
        return None
    return sorted_arr[-2]

# Approach 2: Single-Pass Scan (Optimized for Interviews)
# Time Complexity: O(n)
# Space Complexity: O(1)
def second_largest_optimal(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None

# Test cases
test_arr = [1, 2, 4, 6, 10, 9]
print("Array:", test_arr)
print("Second Largest (Sorting):", second_largest_sorting(test_arr))
print("Second Largest (Optimal):", second_largest_optimal(test_arr))

test_duplicates = [10, 10, 8, 5]
print("Array with Duplicates:", test_duplicates)
print("Second Largest (Optimal):", second_largest_optimal(test_duplicates))
