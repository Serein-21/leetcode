# Last updated: 1/2/2026, 12:18:06 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def make_lls_equal(l1, l2):

    p1, p2 = l1, l2

    while p1 or p2:

        if p1:

            p1 = p1.next

        else:

            n = ListNode(0)
            n.next = l1
            l1 = n

        if p2:

            p2 = p2.next

        else:

            n = ListNode(0)
            n.next = l2
            l2 = n

    return (l1, l2)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Ensure both lists are not empty
        if not l1:
            return l2
        if not l2:
            return l1

        # Make the two linked lists of equal length
        l1, l2 = make_lls_equal(l1, l2)
        any_l2 = True

        while any_l2:
            any_l2 = False
            l1_p, l2_p = l1, l2
            prev = None

            while l1_p:
                # Sum the values of the two nodes and update the current node's value
                k = l1_p.val + l2_p.val
                l1_p.val = k % 10
                l2_p.val = k // 10
                any_l2 = any_l2 or bool(l2_p.val)

                # Move to the next nodes
                prev = l2_p
                l2_p, l1_p = l2_p.next, l1_p.next

            # If there's a carry left in l2, append a new node
            prev.next = ListNode(0)

            # If the sum requires an additional digit, handle it by adding new nodes
            if l2.val:
                n = ListNode(0)
                n.next = l1
                l1 = n
            else:
                l2 = l2.next

        return l1 


        