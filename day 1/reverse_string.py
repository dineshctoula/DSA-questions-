# Question: Write a function to reverse a given string.

# Approach 1: Pythonic Slicing (Recommended for quick use)
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string_slicing(s: str) -> str:
    return s[::-1]

# Approach 2: Iterative / Loop (Shows basic algorithm logic)
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string_iterative(s: str) -> str:
    reversed_str = ""
    # Loop backwards from the end of the string to the start
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

# Test cases
test_input = "dinesh"
print("Input:", test_input)
print("Reversed (Slicing):", reverse_string_slicing(test_input))
print("Reversed (Iterative):", reverse_string_iterative(test_input))
