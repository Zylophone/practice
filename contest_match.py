class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        arr = []
        for i in range(1, n + 1):
            arr.append(i)

        while len(arr) != 1:
            tmp = []
            for i in range(0, len(arr) / 2):
                pair_str = '({},{})'.format(arr[i], arr[-i - 1])
                tmp.append(pair_str)
            arr = tmp
        return arr[0]

print Solution().findContestMatch(8)
