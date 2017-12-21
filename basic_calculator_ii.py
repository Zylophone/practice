class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, sign = 0, '+'
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == ' ':
                continue
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    if stack[-1] * num < 0:
                        stack[-1] = -(abs(stack[-1]) / abs(num))
                    else:
                        stack[-1] = stack[-1] / num
                sign = c
                num = 0
        if not stack:
            return num
        if sign == '+':
            stack[-1] = stack[-1] + num
        elif sign == '-':
            stack[-1] = stack[-1] - num
        elif sign == '*':
            stack[-1] = stack[-1] * num
        else:
            if stack[-1] * num < 0:
                stack[-1] = -(abs(stack[-1]) / abs(num))
            else:
                stack[-1] = stack[-1]/num

        result = sum(stack)
        return result

print Solution().calculate("1*2-3/4+5*6-7*8+9/10")
