class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        max_val, min_val = num, num

    # Try replacing one digit x with 9 to maximize the number
        for digit in '0123456789':
            if digit == '9':
                continue
            replaced = num_str.replace(digit, '9')
            if replaced[0] != '0':
                max_val = max(max_val, int(replaced))

    # Try replacing one digit x with 0 or 1 to minimize the number
        for digit in '123456789':  # avoid replacing 0 to prevent leading zeros
            for to_digit in '0123456789':
                if digit == to_digit:
                    continue
                replaced = num_str.replace(digit, to_digit)
                if replaced[0] != '0':
                    min_val = min(min_val, int(replaced))

        return max_val - min_val
        