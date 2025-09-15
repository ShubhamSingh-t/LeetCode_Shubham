class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0

        for word in text.split():
            if all(char not in broken for char in word):
                count += 1

        return count

        