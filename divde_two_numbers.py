class Solution(object):
    def divide(self, a, b):
        if b == 0:
            return 1e9
        if a == 0:
            return 0

        is_pos = (a > 0 and b > 0) or (a < 0 and b < 0)
        a = abs(a)
        b = abs(b)
        res = 0
        while a > b:
            factor = 0
            while a > b << factor:
                factor += 1
            factor -= 1
            res += 1 << factor
            a -= b << factor
        return res if is_pos else -res


print Solution().divide(100, -3)
