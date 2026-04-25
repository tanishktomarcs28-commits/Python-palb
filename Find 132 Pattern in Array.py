class Solution:
    def has132Pattern(self, arr):
        # code here 
        class Solution:
    def find132pattern(self, arr):
        n = len(arr)
        stack = []
        third = float('-inf')  # this will be arr[k]
        
        for i in range(n - 1, -1, -1):
            # if we find arr[i] < third → 132 pattern found
            if arr[i] < third:
                return True
            
            # update 'third'
            while stack and arr[i] > stack[-1]:
                third = stack.pop()
            
            stack.append(arr[i])
        
        return False
