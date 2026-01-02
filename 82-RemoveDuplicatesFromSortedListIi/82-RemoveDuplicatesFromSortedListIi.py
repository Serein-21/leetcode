# Last updated: 1/2/2026, 12:18:47 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head :
            return head 
        
        p=ListNode(0)
        p.next=head
        head=p

        l=r=head.next

        while r:
            if l.val == r.val:
                r=r.next
            
            elif l.next is r:
                p.next=l
                p=l
                l=r
            else :
                l=r

        p.next= None if l.next else l 
        return head.next
                

        