# Question: Write a function to check if a string is a palindrome.

# Approach 1: Pythonic Slicing (Clean & Simple)
# Time Complexity: O(n)
# Space Complexity: O(n) due to creating a reversed copy
def is_palindrome_slicing(s: str) -> bool:
    return s == s[::-1]

# Approach 2: Two-Pointer Approach (Excellent for interviews)
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary space (no extra string created)
def is_palindrome_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test cases
test_input = "madam"
print(f"Is '{test_input}' a palindrome? (Slicing):", is_palindrome_slicing(test_input))
print(f"Is '{test_input}' a palindrome? (Two-pointer):", is_palindrome_pointers(test_input))

test_input_2 = "hello"
print(f"Is '{test_input_2}' a palindrome? (Two-pointer):", is_palindrome_pointers(test_input_2))
