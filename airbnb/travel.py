import sys

# You're in a ski tournament, where you ski from top of the mountain to one of the
# finish checkpoints at the bottom. There are multiple routes with checkpoints 
# (each checkpoint has an associated point with it). And your total score = 
# (points from all checkpoints you visited - time of your travel). 

# Given: A List of lists, that consists [start_cp, end_cp, time_to_travel]
#        A list of lists, that consists [cp, point]
# Goal: Find the maximum score that you can collect during the tournament and print
# out the optimal path.  


#                  START[0]
#                   / | \
#                  5  6  10
#                 /   |   \
#              A[24] B[3] C[10]
#                 \   |   /|
#                  4  5  6 5
#                   \ | /  |
#                    D[7] E[24]
#                      \   |
#                       3  1
#                        \ |
#                         F[3]
#                         / \
#                        5  10
#                       /     \
#                   END_1[4]  END_2[7]



# Ruby/Python/js
travel_time = [
    ["START", "A", "5"],
    ["START", "B", "6"],
    ["START", "C", "10"],
    # ["A", "D", "4"],
    ["B", "D", "5"],
    ["C", "D", "6"],
    ["C", "E", "5"],
    ["D", "F", "3"],
    ["E", "F", "1"],
    ["F", "END_1", "5"],
    ["F", "END_2", "10"],
]
points = [
    ["START", "0"],
    ["A", "24"],
    ["B", "3"],
    ["C", "10"],
    ["D", "7"],
    ["E", "24"],
    ["F", "3"],
    ["END_1", "4"],
    ["END_2", "7"],
]


class Node(object):
    def __init__(self, x, point):
        self.x = x
        self.point = point
        self.max_score = -sys.maxint
        self.next_stop = {}


def traverse(travel_time, points):
    nodes = {}

    for x, point in points:
        nodes[x] = Node(x, int(point))

    for start, end, score in travel_time:
        nodes[start].next_stop[nodes[end]] = int(score)

    node = nodes['START']
    node.max_score = 0
    result = [-sys.maxint]
    result_path = [None]

    def dfs(node, current, path):
        if node.x.startswith('END_'):
            score = current + node.point
            if score > result[0]:
                result[0] = score
                result_path[0] = path
                print result_path

        for next_node, used_point in node.next_stop.iteritems():
            score = current - used_point + node.point
            dfs(next_node, score, path + [next_node.x])

    dfs(node, 0, ['START'])
    return result[0], result_path


print traverse(travel_time, points)