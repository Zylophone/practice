import collections


class Solution(object):
    '''
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        time = 0
        while True:
            top_n = cnt.most_common(n + 1)
            for c, num in top_n:
                if cnt[c] == 1:
                    del cnt[c]
                else:
                    cnt[c] -= 1
            if not cnt:
                return time + len(top_n)
            else:
                time += n + 1
    '''

    def leastInterval(self, tasks, n):
        c = [0] * 26
        for t in tasks:
            c[ord(t) - ord('A')] += 1
        c.sort()
        i = 25
        while i >= 0 and c[i] == c[25]:
            i -= 1
        return max(len(tasks), (c[25] - 1) * (n + 1) + 25 - i)


# print Solution().leastInterval(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'E'], 5)
print Solution().leastInterval(list('AAABBB'), 2)
import bisect