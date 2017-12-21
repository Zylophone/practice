def palindromePairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    m = set(words)
    result = set()
    for w in words:
        for i in range(len(w) + 1):
            prefix, suffix = w[:i], w[i:]
            rev_prefix = prefix[::-1]
            if is_palindrome(suffix) and rev_prefix in m and rev_prefix != w:
                result.add((w, rev_prefix))

            rev_suffix = suffix[::-1]
            if is_palindrome(prefix) and rev_suffix in m and rev_suffix != w:
                result.add((rev_suffix, w))
    return list(result)


def is_palindrome(w):
    i, j = 0, len(w) - 1
    while i < j:
        if w[i] != w[j]:
            return False
        i += 1
        j -= 1
    return True


print palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
