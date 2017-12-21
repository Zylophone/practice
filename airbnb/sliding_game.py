import heapq
from copy import deepcopy

target = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '-']]


def can_solve(matrix):
    queue = [(-score(matrix), matrix)]
    visited = set()
    while queue:
        c, matrix = heapq.heappop(queue)
        # print c
        # print_board(matrix)
        if matrix == target:
            return True
        for board in next_step(matrix):
            s = serialize(board)
            if s in visited:
                continue
            visited.add(s)
            heapq.heappush(queue, (-score(board), board))
    return False


def serialize(matrix):
    return ''.join([''.join(row) for row in matrix])


def print_board(matrix):
    for row in matrix:
        print ' '.join(row)


def score(matrix):
    cnt = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target[i][j]:
                cnt += 1
    return cnt


def next_step(matrix):
    position = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '-':
                position = i, j
    if not position:
        return []
    i, j = position
    result = []
    if i > 0:
        new_board = deepcopy(matrix)
        new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
        result.append(new_board)
    if j > 0:
        new_board = deepcopy(matrix)
        new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        result.append(new_board)
    if i < len(matrix) - 1:
        new_board = deepcopy(matrix)
        new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
        result.append(new_board)
    if j < len(matrix[0]) - 1:
        new_board = deepcopy(matrix)
        new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]
        result.append(new_board)
    return result


print can_solve([['2', '3', '6'], ['1', '5', '-'], ['4', '7', '8']])
