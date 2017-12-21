class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        m = 0
        d = {}
        for i in range(0, len(s)):
            if s[i] in d:
                j = max(j, d[s[i]] + 1)
            d[s[i]] = i
            m = max(m, i - j + 1)
        return m


#aa

# d = {'a': 0}