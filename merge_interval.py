# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        intervals = sorted(sorted(intervals, key=lambda k: k.end), key=lambda k: k.start)
        for i in intervals:
            if not result:
                result.append(i)
                continue

            if result[-1].end >= i.start:
                result[-1].end = max(i.end, result[-1].end)
            else:
                result.append(i)
        return result
