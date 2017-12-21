class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        r = s[::-1]
        l = self.get_max_len(s + '#' + r)[-1]
        prefix = r[0:len(s) - l] if len(s) - l > 0 else ''
        return prefix + s

    def get_max_len(self, s):
        arr = [0] * len(s)
        i, j = 1, 0
        while i < len(s):
            if s[i] == s[j]:
                arr[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = arr[j - 1]
                else:
                    arr[i] = 0
                    i += 1
        return arr


s = Solution()
print s.shortestPalindrome("aabba")
