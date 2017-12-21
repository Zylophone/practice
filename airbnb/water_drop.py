def pour_water(height, num, position):
    if not height:
        return
    water = [0] * len(height)

    def get_height(p):
        return height[p] + water[p]

    for i in range(num):
        p = position
        while p > 0:
            if get_height(p - 1) <= get_height(p):
                p -= 1
            else:
                break
        left_p = p

        p = position
        while p < len(height) - 1:
            if get_height(p + 1) <= get_height(p):
                p += 1
            else:
                break
        right_p = p

        if get_height(left_p) <= get_height(position) and get_height(left_p) <= get_height(right_p):
            water[left_p] += 1
        elif get_height(right_p) <= get_height(position):
            water[right_p] += 1
        else:
            water[position] += 1

    def print_water():
        sum_arr = [height[i] + water[i] for i in range(len(height))]
        max_height = max(sum_arr)
        for h in range(max_height, -1, -1):
            for i in range(len(height)):
                if get_height(i) < h:
                    print ' ',
                elif height[i] < h:
                    print 'W',
                else:
                    print '+',
            print
    print_water()


pour_water([5, 4, 2, 1, 2, 2, 2, 1, 0, 1, 2, 4], 30, 5)
