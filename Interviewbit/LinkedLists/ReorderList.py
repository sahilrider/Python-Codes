'''https://www.interviewbit.com/problems/reorder-list/'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        t = A
        stack = []
        while(t is not None):
            stack.append(t)
            t = t.next
        n = len(stack)
        t = A
        for i in range(n//2):
            temp = t.next
            t.next = stack.pop()
            t = t.next
            t.next = temp
            t = t.next
        t.next = None
        return A