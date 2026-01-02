# Last updated: 1/2/2026, 12:18:56 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"(": ")", "{": "}", "[": "]"}

        for el in s:
            if el in m:  # If it's an opening bracket
                stack.append(el)
            else:
                if len(stack) == 0:
                    return False
                elif m[stack[-1]] == el:  # Check if the current character matches the last opening bracket
                    stack.pop()
                else:
                    return False

        return len(stack) == 0  # If the stack is empty, all brackets are properly closed
