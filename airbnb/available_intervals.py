def get_intervals(l):
    intervals = []
    for lists in l:
        for interval in lists:
            intervals.append((interval[0], True))
            intervals.append((interval[1], False))
    intervals = sorted(intervals)
    busy = 0
    result = []
    interval = [-1, -1]
    for time, is_start in intervals:
        if is_start:
            if busy == 0 and interval[0] != -1:
                interval[1] = time
                result.append(interval)
                interval = [-1, -1]
            busy += 1
        else:
            busy -= 1

        if busy == 0:
            interval[0] = time
    return result


print get_intervals([[[1, 3], [6, 7]], [[2, 4]], [[2, 3], [9, 12]]])
