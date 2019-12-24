'''https://www.interviewbit.com/problems/add-two-numbers-as-lists/'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        C = ListNode(0)
        curr = C
        carry = 0
        while(A is not None and B is not None):
            # print(A.val)
            val = A.val+B.val+carry
            A = A.next
            B = B.next
            if val<10:
                temp = ListNode(val)
                carry = 0
            else:
                temp = ListNode(val-10)
                carry = 1
            curr.next = temp
            curr = curr.next
        while(A is not None):
            # print(A.val)
            val = A.val+carry
            A = A.next
            if val<10:
                carry = 0
                curr.next = ListNode(val)
            else:
                carry = 1
                curr.next = ListNode(val-10)
            curr = curr.next
        while(B is not None):
            val = B.val+carry
            B = B.next
            if val<10:
                carry = 0
                curr.next = ListNode(val)
            else:
                carry = 1
                curr.next = ListNode(val-10)
            curr = curr.next
        return C.next   
