class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        max_val = num
        min_val = num

        for from_digit in '0123456789':
            for to_digit in '0123456789':
                # Remap from_digit to to_digit
                if from_digit == to_digit:
                    continue
                remapped = num_str.replace(from_digit, to_digit)
                remapped_val = int(remapped)
                max_val = max(max_val, remapped_val)
                min_val = min(min_val, remapped_val)

        return max_val - min_val