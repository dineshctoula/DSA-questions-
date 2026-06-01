# Question: Find the largest number in a given array.

# Approach 1: Manual Iteration (Basic algorithmic approach)
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_largest_iterative(arr):
    if not arr:
        return None  # Handle empty array case
    
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Approach 2: Python Built-in max() (Clean & Pythonic)
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_largest_builtin(arr):
    return max(arr) if arr else None

# Test cases
test_arr = [3, 5, 7, 2, 8]
print("Array:", test_arr)
print("Largest (Iterative):", find_largest_iterative(test_arr))
print("Largest (Built-in):", find_largest_builtin(test_arr))
