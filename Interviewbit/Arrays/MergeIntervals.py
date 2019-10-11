# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
 
class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        new_interval.start= min(new_interval.start,new_interval.end)
        new_interval.end=max(new_interval.start,new_interval.end)
        if len(intervals)==0:
            return [new_interval]
        if new_interval.start<=intervals[0].start and new_interval.end>=intervals[-1].end:
            return [new_interval]
        intervals.append(new_interval)
        intervals.sort(key=lambda l:l.start)
        res =[]
        for i in intervals:
            
            if not res or res[-1].end<i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end,i.end)
            # print([(j.start,j.end) for j in res])
        return res