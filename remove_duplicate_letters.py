import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        stack = []
        for c in s:
            counter[c] -= 1

            if c in stack:
                continue

            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                stack.pop(-1)

            stack.append(c)
        return ''.join(stack)


print Solution().removeDuplicateLetters('cbabc')
