class Solution(object):
    def longestParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        m = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    continue
                else:
                    stack.pop()
                    if not stack:
                        idx = 0
                    else:
                        idx = stack[-1] + 1
                    m = max(m, i - idx + 1)
        return m

s = Solution()
print s.longestParentheses('((()()(()')

