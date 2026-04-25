class Solution:
    def kthSmallest(self, arr, k):
        # Code hereclass Solution:
        arr.sort()
        return arr[k - 1]
        
        
