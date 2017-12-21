import bisect
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result, number, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                number = 10 * number + int(c)
            elif c == '+':
                result += sign * number
                number, sign = 0, 1
            elif c == '-':
                result += sign * number
                number, sign = 0, -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()

        if number != 0:
            result += sign * number
        return result


print Solution().calculate("(1)")
