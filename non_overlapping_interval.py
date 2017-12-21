# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) < 2:
            return 0
        intervals = sorted(intervals, key=lambda i: i.end)
        end = intervals[0].end
        overlapped = 0
        for i in range(1, len(intervals)):
            if intervals[i].start < end:
                overlapped += 1
            else:
                end = intervals[i].end
        return overlapped


print Solution().eraseOverlapIntervals([Interval(1, 100), Interval(11, 22), Interval(1, 11), Interval(2, 12)])
