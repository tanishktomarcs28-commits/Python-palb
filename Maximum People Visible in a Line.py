class Solution:
    def maxVisible(self, arr):
        n = len(arr)
        
        left = [0] * n
        right = [0] * n
        
        # LEFT SIDE
        stack = []
        for i in range(n):
            count = 0
            
            while stack and stack[-1][0] < arr[i]:
                count += stack[-1][1]
                stack.pop()
            
            if stack:
                count += 1
            
            left[i] = count
            stack.append((arr[i], count + 1))
        
        # RIGHT SIDE
        stack = []
        for i in range(n - 1, -1, -1):
            count = 0
            
            while stack and stack[-1][0] < arr[i]:
                count += stack[-1][1]
                stack.pop()
            
            if stack:
                count += 1
            
            right[i] = count
            stack.append((arr[i], count + 1))
        
        # RESULT
        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] + 1)
        
        return ans
