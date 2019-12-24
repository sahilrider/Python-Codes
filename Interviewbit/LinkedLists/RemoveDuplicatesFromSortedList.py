'''https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplicates(self, A):
        temp = A
        while(temp.next !=None):
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return A