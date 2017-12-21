from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ''

        need_char = Counter()
        had_char = Counter()
        for c in t:
            need_char[c] += 1
        min_i, min_j = -1, -1
        m = 1000000
        matched = 0
        j = 0
        for i, c in enumerate(s):
            if c in need_char:
                had_char[c] += 1
                if need_char[c] >= had_char[c]:
                    matched += 1

            if matched < len(t):
                continue

            while j < i:
                if s[j] not in need_char or had_char[s[j]] > need_char[s[j]]:
                    if had_char[s[j]] > need_char[s[j]]:
                        had_char[s[j]] -= 1
                    j += 1
                else:
                    break

            if i - j < m:
                min_i = i
                min_j = j
                m = i - j
        if min_i == -1:
            return ''
        else:
            return s[min_j: min_i + 1]


s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")
