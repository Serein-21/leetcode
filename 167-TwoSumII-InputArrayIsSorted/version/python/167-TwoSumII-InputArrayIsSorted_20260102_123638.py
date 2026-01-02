# Last updated: 1/2/2026, 12:36:38 PM
'''
"""
    APPROACH: Two Pointers (Input Array Is Sorted)
    ----------------------------------------------
    
    INTUITION:
    Because the array is sorted, we can determine directionality:
    - Moving the right pointer (j) left ALWAYS decreases the sum.
    - Moving the left pointer (i) right ALWAYS increases the sum.
    We start at opposite ends to "narrow down" the search space efficiently.

    ALGORITHM:
    1. Initialize two pointers: 'i' at the start (0) and 'j' at the end (n-1).
    2. Loop while i < j:
       - Calculate 'current_sum = numbers[i] + numbers[j]'.
       - CASE A (Match): If current_sum == target, return indices immediately.
       - CASE B (Too Large): If current_sum > target, decrement 'j' to reduce the sum.
       - CASE C (Too Small): If current_sum < target, increment 'i' to increase the sum.

    COMPLEXITY:
    - Time: O(n) ... We process each element at most once.
    - Space: O(1) ... We only use two integer variables for pointers.

    COMMON PITFALLS:
    - Infinite Loop: Failing to move pointers (i++ or j--) or break/return after finding a match.
    - Indexing: Problem usually requires 1-based indexing (return i+1, j+1).
    """
'''

1from typing import List
2
3class Solution:
4    def twoSum(self, numbers: List[int], target: int) -> List[int]:
5        # Initialize pointers
6        i = 0
7        j = len(numbers) - 1
8        
9        while i < j:
10            current_sum = numbers[i] + numbers[j]
11            
12            if current_sum == target:
13                # Return immediately. 
14                # The problem uses 1-based indexing, so we add 1.
15                return [i + 1, j + 1]
16            
17            elif current_sum > target:
18                # If sum is too large, move the right pointer to the left
19                j -= 1
20            
21            else:
22                # If sum is too small, move the left pointer to the right
23                i += 1
24                
25        # Return an empty list if no solution is found
26        return []
27
28        
29
30        