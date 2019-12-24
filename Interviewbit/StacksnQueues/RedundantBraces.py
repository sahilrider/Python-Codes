'''https://www.interviewbit.com/problems/redundant-braces/'''

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        op = ['+', '-', '*', '/']
        for i in A:
            if i=='(' or i in op:
                stack.append(i)
            elif i==')':
                t = stack.pop()
                if t=='(':
                    return 1
                else:
                    stack.pop()
        return 0