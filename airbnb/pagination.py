class Solution(object):
    def pagination(self, n, l):
        results = []
        page = []
        while l:
            while len(page) < n and l:
                existed_ids = set()
                i = 0
                while i < len(l):
                    id = l[i].split(',')[0]
                    if id not in existed_ids:
                        existed_ids.add(id)
                        page.append(l[i])
                        l.pop(i)
                        if len(page) >= n:
                            break
                    else:
                        i += 1
            results.append(page)
            page = []
        if page:
            results.append(page)
        return results



print Solution().pagination(5, [
    "1,28,310.6,SF",
    "4,5,204.1,SF",
    "20,7,203.2,Oakland",
    "6,8,202.2,SF",
    "6,10,199.1,SF",
    "1,16,190.4,SF",
    "6,29,185.2,SF",
    "7,20,180.1,SF",
    "6,21,162.1,SF",
    "2,18,161.2,SF",
    "2,30,149.1,SF",
    "3,76,146.2,SF",
    "2,14,141.1,San	Jose"])
