'''https://www.interviewbit.com/problems/sort-list/'''

class Solution:
# @param A : head node of linked list
# @return the head node in the linked list
    def sortList(self, A):
        if not A or not A.next:
            return A
        first, second = self.divide(A)
        first = self.sortList(first)
        second = self.sortList(second)
        return self.merge(first, second)
    
    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first
        left, right = first, second
        if left.val <= right.val:
            cur, head = left, first
            left = left.next
        else:
            cur, head = right, second
            right = right.next
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return head
    
    def divide(self, head):
        fast, slow = head.next, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        second_part = slow.next
        slow.next = None
        return head, second_part
