# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
 
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda l:l.start)
        stack=[intervals[0].start,intervals[0].end]
        for i in intervals[1:]:
            # print(stack)
            if i.start>stack[-1]:
                stack.append(i.start)
                stack.append(i.end)
            else:
                t2=stack.pop()
                t1=stack.pop()
                stack.append(min(t1,i.start))
                stack.append(max(t2,i.end))
        # print(stack)
        res=[]
        for i in range(0,len(stack),2):
            res.append(Interval(s=stack[i],e=stack[i+1]))
        return res