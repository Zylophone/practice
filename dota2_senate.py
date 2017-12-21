class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r = []
        d = []
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            if r[0] < d[0]:
                d = d[1:]
                r = r[1:] + [r[0] + len(senate)]
            else:
                r = r[1:]
                d = d[1:] + [d[0] + len(senate)]
        return 'Radiant' if r else 'Dire'

print Solution().predictPartyVictory('RDD')