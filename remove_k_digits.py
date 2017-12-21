class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out = []
        for d in num:
            while k > 0 and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        if k > 0:
            out = out[:-k]
        out = ''.join(out).lstrip('0')

        return out or '0'

print Solution().removeKdigits('1432219', 3)

