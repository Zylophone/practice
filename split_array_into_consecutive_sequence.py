import collections
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ct = collections.Counter()
        appendedCt = collections.Counter()
        for i in nums:
            ct[i] += 1
        for i in nums:
            if ct[i] == 0:
                continue
            elif appendedCt[i] > 0:
                appendedCt[i] -= 1
                appendedCt[i + 1] += 1
            elif ct[i + 1] > 0 and ct[i + 2] > 0:
                ct[i + 1] -= 1
                ct[i + 2] -= 1
                appendedCt[i + 3] += 1
            else:
                return False
            ct[i] -= 1
        return T
