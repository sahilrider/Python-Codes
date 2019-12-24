'''https://www.interviewbit.com/problems/min-stack/'''

class MinStack:
    def __init__(self):
        self.t = -1
        self.stack = []
        self.minstack = []
        
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if self.t==-1:
            self.minstack.append(x)
        else:
            if x<self.minstack[self.t]:
                self.minstack.append(x)
            else:
                self.minstack.append(self.minstack[self.t])
        self.t+=1
        # print(self.stack, self.minstack, self.t)

    # @return nothing
    def pop(self):
        if self.t==-1:
            return
        self.minstack.pop()
        self.stack.pop()
        self.t-=1

    # @return an integer
    def top(self):
        # print('Inside func')
        if self.t==-1:
            # print('Inside if')
            return -1
        # print('Return val')
        return self.stack[self.t]
        
    # @return an integer
    def getMin(self):
        # print('fadswf')
        if self.t==-1:
            return -1
        else:
            # print(self.minstack[-1])
            return self.minstack[-1]

