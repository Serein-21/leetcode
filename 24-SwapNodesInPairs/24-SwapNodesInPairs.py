# Last updated: 1/2/2026, 12:18:55 PM
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        """
        Swaps every two adjacent nodes in a singly-linked list.

        Args:
            head: The head of the singly-linked list.

        Returns:
            The head of the modified list with swapped pairs.
        """

        if not head or not head.next:  # Handle cases with less than two nodes
            return head

        dummy = ListNode(0)  # Create a dummy node for convenience
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            # Swap the next pointers of the current pair
            nextPair = curr.next.next
            curr.next.next = curr
            prev.next = curr.next
            curr.next = nextPair

            # Move to the next pair (if it exists)
            prev = curr
            curr = nextPair

        return dummy.next