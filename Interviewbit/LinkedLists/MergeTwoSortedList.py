'''https://www.interviewbit.com/problems/merge-two-sorted-lists/'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        C = ListNode(0)
        curr = C
        while A.next!=None and B.next!=None:
            if A.val<=B.val:
                curr.next = ListNode(A.val)
                curr = curr.next
                A = A.next
            else:
                curr.next = ListNode(B.val)
                curr = curr.next
                B = B.next
        if A!=None:
            curr.next = A
        if B!=None:
            curr.next = B
        return C.next