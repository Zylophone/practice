class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        num = str(num)
        if len(num) < 2:
            return int(num)
        num = list(num)
        sorted_num = sorted(num, reverse=True)
        for i in range(len(num)):
            if num[i] == sorted_num[i]:
                continue
            for j in range(len(num) - 1, -1, -1):
                if sorted_num[i] == num[j]:
                    num[i], num[j] = num[j], num[i]
                    break
            break
        return int(''.join(num))


print Solution().maximumSwap(2736)