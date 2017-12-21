from collections import Counter


class Solution(object):
    def minString(self, s):
        ct = Counter()
        i, j = 0, 0
        unique = 0
        start, end = -1, -1
        while i < len(s):
            if ct.get(s[i], 0) == 0 and unique >= 2:
                if i - j > end - start:
                    start, end = j, i

                    while True:
                        ct[s[j]] -= 1
                        j += 1
                        if ct[s[j]] == 0:
                            unique -= 1
                            break

            if ct.get(s[i], 0) == 0:
                unique += 1
            ct[s[i]] += 1
            i += 1

        if i - j > end - start:
            start, end = j, i

        return s[start: end]


print Solution().minString('ababcbcbc')