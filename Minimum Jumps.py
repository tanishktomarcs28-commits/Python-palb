class Solution:
	def minJumps(self, arr):
	    # code here
        n = len(arr)
        
        # edge cases
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 1
        maxReach = arr[0]
        steps = arr[0]
        
        for i in range(1, n):
            
            # reached end
            if i == n - 1:
                return jumps
            
            maxReach = max(maxReach, i + arr[i])
            steps -= 1
            
            # no steps left → jump
            if steps == 0:
                jumps += 1
                
                if i >= maxReach:
                    return -1
                
                steps = maxReach - i
        
        return -1
	    
