class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        n = len(arr)
        
        curr_sum = 0
        min_len = n + 1
        start = 0
        
        for end in range(n):
            curr_sum += arr[end]
            
            while curr_sum >= x:   # FIX HERE
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1
        
        return 0 if min_len == n + 1 else min_len
