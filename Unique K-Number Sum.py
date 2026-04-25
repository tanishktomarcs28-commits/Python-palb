class Solution:
    def combinationSum(self, k, n):
        result = []
        
        def backtrack(start, path, remaining):
            # valid combination
            if len(path) == k and remaining == 0:
                result.append(path[:])
                return
            
            # invalid cases
            if len(path) > k or remaining < 0:
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()
        
        backtrack(1, [], n)
        return result
