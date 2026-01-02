# Last updated: 1/2/2026, 12:18:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None:  
            return None 

        
        if head.next is None and head.val == val:
            return None 
        
      
        sentinel = ListNode(0) 
        sentinel.next = head
        
        
        current_prev = sentinel
      
        pointer = head 
        
        while pointer:
            if pointer.val == val:
                
                current_prev.next = pointer.next
                
                
                pointer = current_prev.next 
            else:
               
                current_prev = pointer 
                
                
                pointer = pointer.next
                
       
        return sentinel.next 