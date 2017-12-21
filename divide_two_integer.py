class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = abs(dividend)
        if divisor < 0:
            sign = -sign
            divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            multi = 1
            tmp = divisor
            while dividend >= tmp:
                dividend -= tmp
                result += multi
                multi <<= 1
                tmp <<= 1
        return sign * result


print Solution().divide(-2147483648, -1)