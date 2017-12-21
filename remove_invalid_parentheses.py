class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        queue = [s]
        next_queue = []
        ans = []
        visited = set()
        done = False
        while queue:
            for t in queue:
                miss_count = self.miss(t)
                if miss_count == 0:
                    ans.append(t)
                    done = True
                else:
                    for i in range(len(t)):
                        if t[i] != '(' and t[i] != ')':
                            continue
                        ns = t[:i] + t[i + 1:]
                        if ns not in visited and self.miss(ns) < miss_count:
                            next_queue.append(ns)
                            visited.add(ns)
            if done:
                return ans
            queue = next_queue
            next_queue = []
        return ans

    def miss(self, s):
        a = b = 0
        for c in s:
            a += {'(': 1, ')': -1}.get(c, 0)
            b += a < 0
            a = max(a, 0)
        return a + b
