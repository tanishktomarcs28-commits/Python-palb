class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        from typing import List
        result = []

        def backtrack(start, path, target):
            # Base case
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return
            
            # Try all candidates from current index
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # choose
                backtrack(i, path, target - candidates[i])  # reuse allowed
                path.pop()  # backtrack

        backtrack(0, [], target)
        return result
