# Definition for an interval.
import bisect


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        l = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            idx = bisect.bisect_left(l, (e.end,))
            res.append(l[idx][1] if idx < len(l) else -1)
        return res
