class Solution:
    def prevGreater(self, arr):
        stack = []
        result = []

        for num in arr:
            # Remove elements <= current
            while stack and stack[-1] <= num:
                stack.pop()
            
            # If stack empty → no greater element
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            # Push current element
            stack.append(num)

        return result
