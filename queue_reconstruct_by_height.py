class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(sorted(people, key=lambda p: p[1]), key=lambda p: p[0], reverse=True)
        result = []
        for height, rank in people:
            result.insert(rank, (height, rank))
        return result


print Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
