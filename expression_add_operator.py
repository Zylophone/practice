class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def isLeadingZeros(num):
            return len(num) > 1 and num.startswith('0')

        def solve(num, target, mulExpr='', mulVal=1):
            ans = []
            if not isLeadingZeros(num) and int(num) * mulVal == target:
                ans.append(num + mulExpr)
            for i in range(1, len(num)):
                lnum, rnum = num[:i], num[i:]

                if isLeadingZeros(rnum):
                    continue
                right, rightVal = rnum + mulExpr, int(rnum) * mulVal
                for left in solve(lnum, target - rightVal):
                    ans.append(left + '+' + right)
                for left in solve(lnum, target + rightVal):
                    ans.append(left + '-' + right)

                for left in solve(lnum, target, '*' + right, rightVal):
                    ans.append(left)
            return ans

        if not num:
            return []
        return solve(num, target)


print Solution().addOperators("000", 0)
