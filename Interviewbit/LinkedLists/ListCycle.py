'''https://www.interviewbit.com/problems/list-cycle/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        seen = []
        temp = A
        while(temp!=None):
            if str(temp.val)[-1] != 's':
                temp.val = str(temp.val)+'s'
                temp = temp.next
            else:
                temp.val = int(temp.val[:-1])
                return temp
        return None