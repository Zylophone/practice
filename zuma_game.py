from collections import Counter


class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        remains = Counter()
        for c in hand:
            remains[c] += 1
        min_step = [-1]
        self.run(board, remains, 0, min_step)
        return min_step[0]

    def run(self, board, remains, cur_step, min_step):
        board = self.crash(board)
        if len(board) == 0:
            self.update_min_step(cur_step, min_step)
            return

        for i in xrange(0, len(board)):
            c = board[i]
            if remains.get(c, 0) == 0:
                continue
            new_board = board[0:i + 1] + c + board[i + 1:]
            new_remains = dict(remains)
            new_remains[c] -= 1
            self.run(new_board, new_remains, cur_step + 1, min_step)

    def update_min_step(self, cur_step, min_step):
        if min_step[0] == -1:
            min_step[0] = cur_step
        else:
            min_step[0] = min(min_step[0], cur_step)

    def crash(self, board):
        if len(board) < 3:
            return board
        while True:
            is_crashed = False
            for i in xrange(0, len(board) - 2):
                if board[i] == board[i + 1] == board[i + 2]:
                    is_crashed = True
                    if i + 3 < len(board) and board[i] == board[i + 3]:
                        board = board[0:i] + board[i + 4:]
                    else:
                        board = board[0:i] + board[i + 3:]
                    break
            if not is_crashed:
                break
        return board

s = Solution()
#print s.crash('AABBBAA')
print s.findMinStep('AABBCC', 'GGAB')