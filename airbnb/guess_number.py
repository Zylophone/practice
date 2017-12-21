TARGET = '3232'


def guess_server(nums):
    cnt = 0
    for i in range(4):
        if TARGET[i] == nums[i]:
            cnt += 1
    return cnt


def guess():
    candidates = {}
    cnt = 0
    for i in range(1, 7):
        guess_num = str(i) * 4
        result = guess_server(guess_num)
        if result == 4:
            return guess_num
        if result > 0:
            candidates[i] = result
            cnt += result
        if cnt == 4:
            break

    guess_base = ['0'] * 4
    res = ''
    for i in range(4):
        max_cnt, max_digit = -1, -1
        for k in candidates.keys():
            guess_base[i] = str(k)
            result = guess_server(''.join(guess_base))
            if result > max_cnt:
                max_cnt, max_digit = result, k
        res += str(max_digit)
        candidates[max_digit] -= 1
        if candidates[max_digit] == 0:
            del candidates[max_digit]
    return res
print guess()