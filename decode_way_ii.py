class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0

        first = 1
        if s[0] == '*':
            second = 9
        elif s[0] == '0':
            second = 0
        else:
            second = 1
        for i in range(1, len(s)):
            tmp = second
            if s[i] == '*':
                if s[i - 1] == '1':
                    tmp += 9
                elif s[i - 1] == '2':
                    tmp += 6
                elif s[i - 1] == '*':
                    tmp += 26


print Solution().numDecodings('1*')