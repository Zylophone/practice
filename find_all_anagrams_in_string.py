import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        cp = collections.Counter(list(p))
        counter = collections.Counter()
        for i in range(len(s)):
            counter[s[i]] += 1
            if i >= len(p):
                counter[s[i - len(p)]] -= 1
                if counter[s[i - len(p)]] == 0:
                    del counter[s[i - len(p)]]
            if counter == cp:
                result.append(i - len(p) + 1)
        return result


print Solution().findAnagrams("cbaebabacd", "abc")
