import collections


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = 1
        parts = collections.defaultdict(str)
        digits = collections.defaultdict(int)
        for c in s:
            if c.isdigit():
                digits[k] = digits[k] * 10 + int(c)
            elif c == '[':
                k += 1
            elif c == ']':
                parts[k - 1] += digits[k - 1] * parts[k]
                digits[k - 1] = 0
                parts[k] = ''
                k -= 1
            else:
                parts[k] += c
        return parts[1]


print Solution().decodeString("3[a]2[bc]")
