import heapq
import sys


def get_shortest_path(wizards):
    queue = []
    parents = [-1] * len(wizards)
    distance = [sys.maxint] * len(wizards)
    distance[0] = 0
    heapq.heappush(queue, 0)
    while queue:
        n = -heapq.heappop(queue)
        for next in wizards[n]:
            new_distance = distance[n] + (next - n) * (next - n)
            if new_distance < distance[next]:
                distance[next] = new_distance
                parents[next] = n

            heapq.heappush(queue, -next)
            if next == 9:
                break
    path = [9]
    while True:
        parent = parents[path[-1]]
        if parent == -1:
            return []
        path.append(parent)
        if parent == 0:
            break
    path = path[::-1]
    return path


wizards = [
    [1, 4, 5],
    [],
    [],
    [],
    [9],
    [],
    [],
    [],
    [],
    []
]
print get_shortest_path(wizards)