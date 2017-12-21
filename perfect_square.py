class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = []
        for i in range(1, n + 1):
            num = i * i
            if num > n:
                break
            else:
                lst.append(num)

        cnt = 1
        level = {n}
        while level:
            temp = set()
            for num in level:
                for square in lst:
                    if square == num:
                        return cnt
                    elif square > num:
                        break
                    else:
                        temp.add(num - square)
            level = temp
            cnt += 1
        return cnt


print Solution().numSquares(12)
