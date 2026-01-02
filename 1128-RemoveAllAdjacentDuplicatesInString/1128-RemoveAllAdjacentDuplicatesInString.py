# Last updated: 1/2/2026, 12:17:43 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for el in s:
            if stack and el == stack[-1]:  # Check if stack is not empty and the current element is the same as the top element
                stack.pop()  # Remove the top element if it's the same as the current element
            else:
                stack.append(el)  # Otherwise, add the current element to the stack
        return ''.join(stack)  # Convert the stack back into a string and return it
