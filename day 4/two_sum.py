# Question: Given an array of integers and a target sum, return the indices of the two numbers that add up to the target.

# Approach 1: Brute Force (Nested Loops)
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

# Approach 2: Optimized Hash Map (Dictionary) - Recommended for Interviews
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_optimized(arr, target):
    seen = {} # value -> index
    for index, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []

# Test cases
test_arr = [1, 2, 3]
test_target = 4
print("Array:", test_arr, "Target:", test_target)
print("Indices (Brute Force):", two_sum_brute_force(test_arr, test_target))
print("Indices (Optimized):", two_sum_optimized(test_arr, test_target))
