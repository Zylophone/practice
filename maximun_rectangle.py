class Solution(object):
    def maxRectangle(self, m):
        if len(m) == 0:
            return 0
        res = 0
        for i in xrange(0, len(m)):
            height = []
            for j in xrange(0, len(m[i])):
                k = i
                h = 0
                while k < len(m) and m[k][j] == 1:
                    h += 1
                    k += 1
                height.append(h)
            height.append(0)

            s = []
            k = 0
            while k < len(height):
                if not s or height[s[-1]] < height[k]:
                    s.append(k)
                    k += 1
                else:
                    tmp = s.pop(-1)
                    area = height[tmp] * (k if not s else k - s[-1] - i)
                    res = max(res, area)
            return res


m = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print Solution().maxRectangle(m)
