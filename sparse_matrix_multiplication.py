class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        am, an = len(A), len(A[0])
        bm, bn = len(B), len(B[0])
        C = [[0 for _ in xrange(bn)] for _ in xrange(am)]

        for i in range(am):
            for j in range(an):
                if A[i][j]:
                    for k in range(bn):
                        C[i][k] += 0 if not B[j][k] else A[i][j] * B[j][k]
        return C


print Solution().multiply([[1, -5]], [[12], [-1]])
