# Last updated: 1/2/2026, 12:18:40 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pointer = head

        id_map={}
        

        while pointer:

            idp=id(pointer)

            if idp in id_map:

                

                return pointer
            
            
            id_map[idp] = pointer
            pointer=pointer.next
        
        return None
              




        