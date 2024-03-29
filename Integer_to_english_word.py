class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return 'Zero'
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", 'Thousand', 'Million', 'Billion']

        def helper(num):
            if num >= 100:
                return (LESS_THAN_20[num / 100] + ' Hundred ' + helper(num % 100)).strip()
            elif num < 20:
                return LESS_THAN_20[num]
            else:
                return (TENS[num / 10] + ' ' + helper(num % 10)).strip()

        word = ''
        i = 0
        while num > 0:
            if num % 1000 != 0:
                word = helper(num % 1000) + ' ' + THOUSANDS[i] + ' ' + word
            i += 1
            num /= 1000
        return word.strip()






