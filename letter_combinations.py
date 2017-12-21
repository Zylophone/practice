class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz')
        }
        result = []
        if not digits:
            return []

        def dfs(digits, current):
            if not digits:
                result.append(current)
                return
            for c in m.get(digits[0], []):
                dfs(digits[1:], current + c)

        dfs(digits, '')
        return result

print Solution().letterCombinations('2')