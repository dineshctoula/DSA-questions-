# Question: Valid Parentheses (LeetCode 20)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Time Complexity: O(n) - where n is the length of the string, as we traverse it once.
# Space Complexity: O(n) - in the worst case, the stack will store all open brackets.
def is_valid_parentheses(s: str) -> bool:
    # Map each closing bracket to its corresponding open bracket
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Pop the top element from stack if not empty, else use a dummy value '#'
            top_element = stack.pop() if stack else '#'
            
            # If the mapping doesn't match the popped element, it's invalid
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not stack

# Test cases
test_1 = "()[]{}"
test_2 = "([)]"
test_3 = "{[]}"

print(f"Is '{test_1}' valid? : {is_valid_parentheses(test_1)}")
print(f"Is '{test_2}' valid? : {is_valid_parentheses(test_2)}")
print(f"Is '{test_3}' valid? : {is_valid_parentheses(test_3)}")
