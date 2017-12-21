# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left, merge, right = [], [], []
        for i in intervals:
            if i.end < s:
                left.append(i)
            elif i.start > e:
                right.append(i)
            else:
                merge.append(i)

        if merge:
            s = min(s, merge[0].start)
            e = max(e, merge[-1].end)
        return left + [Interval(s, e)] + right


print Solution().insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5))
