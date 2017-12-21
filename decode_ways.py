class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0 or not self.is_valid(s[0]):
            return 0
        count = [1, 1]
        for i in range(0, len(s)):
            tmp = 0
            if self.is_valid(s[i]):
                tmp += count[1]

            if i > 0:
                if self.is_valid(s[i-1:i + 1]):
                    tmp += count[0]
            count[0] = count[1]
            count[1] = tmp
        return count[1]

    def is_valid(self, num_str):
        if num_str[0] == '0':
            return False

        try:
            if 0 <= int(num_str) <= 26:
                return True
            else:
                return False
        except:
            return False

s = Solution()
print s.is_valid('27')
print s.numDecodings('27')