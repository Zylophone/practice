import collections


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        contents = collections.defaultdict(list)
        for path in paths:
            items = path.split(' ')
            for i in range(1, len(items)):
                filename, content = items[i].split('(')
                content = content[:-1]
                contents[content].append(items[0] + '/' + filename)

        return [item for item in contents.values() if len(item) > 1]


print Solution().findDuplicate(
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
