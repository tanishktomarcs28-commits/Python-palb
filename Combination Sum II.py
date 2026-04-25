lass Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from typing import List

        result = []
        candidates.sort()  # important

        def backtrack(start, path, target):
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i])  # move forward
                path.pop()

        backtrack(0, [], target)
        return result
