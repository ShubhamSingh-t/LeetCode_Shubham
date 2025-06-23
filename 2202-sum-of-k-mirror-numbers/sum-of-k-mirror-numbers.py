class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(num, base):
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))

        def generate_decimal_palindromes():
            length = 1
            while True:
                # Odd length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])  # Odd-length
                # Even length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])  # Even-length
                length += 1

        total = 0
        count = 0
        for num in generate_decimal_palindromes():
            if is_palindrome(to_base_k(num, k)):
                total += num
                count += 1
                if count == n:
                    break
        return total
