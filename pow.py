class Solution(object):
    def pow(self, x, n):
        x = float(x)
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return float(1 / self.pow(x, -n))
        if n % 2 == 0:
            return self.pow(x * x, n / 2)
        else:
            return self.pow(x * x, n / 2) * x


print Solution().pow(-3, -4)
