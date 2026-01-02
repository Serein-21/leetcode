# Last updated: 1/2/2026, 12:18:15 PM
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:  # Correct base case condition
            return head 
        
        o = head  # 'o' is the odd node pointer
        e = head.next  # 'e' is the even node pointer
        even_head = e  # Store the head of the even list
        
        # Iterate while there are even and odd nodes left to process
        while e and e.next:
            o.next = e.next  # Link current odd node to the next odd node
            o = o.next  # Move the odd pointer forward
            e.next = o.next  # Link current even node to the next even node
            e = e.next  # Move the even pointer forward
        
        o.next = even_head  # Finally, link the end of the odd list to the head of the even list
        return head
