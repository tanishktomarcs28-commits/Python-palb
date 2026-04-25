class Solution:
    def median(self, mat):
    	# code here 
    	import bisect
        r = len(mat)
        c = len(mat[0])
        
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        
        desired = (r * c) // 2
        
        while low < high:
            mid = (low + high) // 2
            
            # count elements <= mid
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid
        
        return low
    	
