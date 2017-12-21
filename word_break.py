class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        queue = [s]
        visited = {s}
        while queue:
            word = queue.pop(0)
            if word in wordDict:
                return True
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordDict and suffix not in visited:
                    queue.append(suffix)
                    visited.add(suffix)
        return False


print Solution().wordBreak("goalspecial", ["go", "goal", "goals", "special"])
