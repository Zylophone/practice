# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts = sorted(starts)
        ends = sorted(ends)
        rooms, end_index =0, 0
        for i in range(len(intervals)):
            if starts[i] < ends[end_index]:
                rooms += 1
            else:
                end_index += 1
        return rooms


