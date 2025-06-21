class Solution:
    from collections import Counter

    def minimumDeletions(self, word: str, k: int) -> int:
        n = len(word)
        fre_c = Counter(word)
        fre = list(fre_c.values())
        min_d = float('inf')
        for tar in range(1, max(fre)+1):
            deletion = 0
            for i in fre:
                if i < tar:
                    deletion+=i
                elif i> tar+k:
                    deletion += i - (tar+k)
            min_d = min(deletion, min_d)
        return min_d

        