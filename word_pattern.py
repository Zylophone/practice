class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        c_to_item = {}
        item_to_c = {}

        arr = str.split(' ')
        if len(pattern) != len(arr):
            return False

        for i in range(len(pattern)):
            c = pattern[i]
            item = arr[i]
            if c not in c_to_item:
                c_to_item[c] = item
                if item in item_to_c:
                    return False
                else:
                    item_to_c[item] = c
            else:
                if c_to_item.get(c) != item and item_to_c.get(item) != c:
                    return False
        return True

