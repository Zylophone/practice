class Solution(object):
    def fullJustify(self, words, maxWidth):
        result, current, num_of_letter = [], [], 0
        for w in words:
            if len(current) + num_of_letter + len(w) > maxWidth:
                space = maxWidth - num_of_letter
                for i in range(space):
                    current[i % (len(current) - 1 or 1)] += ' '
                result.append(''.join(current))
                current, num_of_letter = [], 0

            current.append(w)
            num_of_letter += len(w)

        line = ' '.join(current)
        line += (maxWidth - len(line)) * ' '
        result.append(line)
        return result


print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 14)
