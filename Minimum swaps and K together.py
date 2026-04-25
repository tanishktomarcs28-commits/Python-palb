#User function Template for python3

class Solution:
        
    def minSwap (self,arr, k) : 
        #Complete the function
        n = len(arr)
        
        # Step 1: Count elements <= k (good elements)
        good = 0
        for num in arr:
            if num <= k:
                good += 1
        
        # Step 2: Count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        # Step 3: Sliding window
        i = 0
        j = good
        
        while j < n:
            # Remove left element
            if arr[i] > k:
                bad -= 1
            
            # Add right element
            if arr[j] > k:
                bad += 1
            
            ans = min(ans, bad)
            
            i += 1
            j += 1
        
        return ans
