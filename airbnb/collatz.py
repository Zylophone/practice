def find_steps(num):
    result = {}

    def helper(num):
        if num in result:
            return result[num]
        if num <= 1:
            return 1
        if num % 2 == 0:
            step = helper(num / 2) + 1
            result[num] = step
        else:
            step = helper(num * 3 + 1) + 1
            result[num] = step
        return num
    m = 1
    for i in range(num):
        m = max(helper(i), m)
    print result
    return m

print find_steps(7)
