# Question: Remove duplicates from a list.

# Approach 1: Order-Preserving O(n) using a Set
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_set(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Approach 2: Pythonic One-liner (Preserves Order)
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_pythonic(arr):
    # dict.fromkeys preserves insertion order while removing duplicates
    return list(dict.fromkeys(arr))

# Approach 3: In-Place for Sorted Array (LeetCode 26 - Two Pointer)
# Modifies the input array in-place and returns the number of unique elements
# Time Complexity: O(n)
# Space Complexity: O(1)
def remove_duplicates_inplace(arr):
    if not arr:
        return 0
    
    # 'write_index' points to the position where the next unique element should go
    write_index = 1
    for r in range(1, len(arr)):
        if arr[r] != arr[r - 1]:
            arr[write_index] = arr[r]
            write_index += 1
            
    return write_index # The first 'write_index' elements are the unique elements

# Test cases
test_arr = [1, 2, 2, 3, 4, 4, 5]
print("Original:", test_arr)
print("Removed Duplicates (Set):", remove_duplicates_set(test_arr))
print("Removed Duplicates (Pythonic):", remove_duplicates_pythonic(test_arr))

# In-place test
unique_count = remove_duplicates_inplace(test_arr)
print("Modified Array (In-place):", test_arr[:unique_count])