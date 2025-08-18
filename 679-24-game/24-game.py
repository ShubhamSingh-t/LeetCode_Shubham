class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        import itertools

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Pick two numbers
                        a, b = nums[i], nums[j]
                        # Remaining numbers
                        rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        # Try all operations
                        for op in [a + b, a - b, b - a, a * b] + ([a / b] if b != 0 else []) + ([b / a] if a != 0 else []):
                            if dfs(rest + [op]):
                                return True
            return False

        return dfs([float(c) for c in cards])
        