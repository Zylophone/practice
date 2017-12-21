def is_substring(s, p):
    if len(p) == 0:
        return True
    if len(s) == 0:
        return False
    arr = get_next_array(p)

    i, j = 0, 0
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = arr[j]

    return j == len(p)


def get_next_array(p):
    arr = [0] * len(p)
    i, j = 1, 0
    while i < len(p):
        if p[i] == p[j]:
            arr[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                j = arr[j - 1]
            else:
                arr[i] = 0
                i += 1
    return arr

'aabaabaaabcd'.find('baaabc')
print is_substring('aabaabaaabcd', 'baaabc')
