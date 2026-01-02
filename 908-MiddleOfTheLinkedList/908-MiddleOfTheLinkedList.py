# Last updated: 1/2/2026, 12:17:47 PM
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head  # Return head instead of None for single node lists
        
        left = head
        right = head

        # Move right pointer by 2 steps and left by 1 step
        while right is not None and right.next is not None:
            right = right.next.next
            left = left.next
        
        # When the loop ends, left is at the middle
        return left
