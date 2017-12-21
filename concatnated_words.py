class Solution(object):
    # trie + dfs or dp
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        words = set(words)
        for word in words:
            if len(word) == 0:
                continue
            dp = [False] * (len(word) + 1)
            dp[0] = True
            for i in range(0, len(dp)):
                if not dp[i]:
                    continue
                for j in range(i + 1, len(dp)):
                    if j - i < len(word) and word[i: j] in words:
                        dp[j] = True
            if dp[-1]:
                result.append(word)
        return result


s = Solution()

print s.findAllConcatenatedWordsInADict(['a', 'b', 'aab', 'abc', 'abb'])
