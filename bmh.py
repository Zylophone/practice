def is_substring(s, p):
    n = len(p)
    i = n
    table = build_table(p)
    print table
    while i <= len(s):
        if s[i - n:i] == p:
            return True
        else:
            skip = table[s[i - 1]] if s[i - 1] in table else n
            i += skip
    return False


def build_table(p):
    table = {}
    n = len(p)
    for i in range(0, n):
        table[p[i]] = n - i - 1
    return table


print is_substring('aabaa', 'baaaa')
