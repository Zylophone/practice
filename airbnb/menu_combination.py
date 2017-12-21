def price_combination(prices, target):
    result = []
    prices = sorted(prices)

    def dfs(current, start, target):
        if equal(target, 0):
            result.append(list(current))
        for i in range(start, len(prices)):
            if i != start and prices[i] == prices[i - 1]:
                continue
            if prices[i] > target and not equal(prices[i], target):
                break
            current.append(prices[i])
            dfs(current, i + 1, target - prices[i])
            current.pop()

    dfs([], 0, target)
    return result


def equal(a, b):
    return abs(a - b) < 0.00001

print price_combination([1.1, 1.1, 2.2, 1.7], 3.9)