class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter

        vowels = set('aeiou')
        freq = Counter(s)

        max_vowel_freq = max((freq[ch] for ch in vowels if ch in freq), default=0)
        max_consonant_freq = max((freq[ch] for ch in freq if ch not in vowels), default=0)

        return max_vowel_freq + max_consonant_freq

            