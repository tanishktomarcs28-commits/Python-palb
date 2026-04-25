class Solution:
    def countElements(self, arr, x):
        n = len(arr)
        
        # Step 1: Find pivot (smallest element index)
        low, high = 0, n - 1
        
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        
        pivot = low
        
        # Helper: count elements ≤ x using binary search
        def count_leq(l, r):
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= x:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return (ans + 1) if ans != -1 else 0
        
        # Step 2: Count in both parts
        count1 = count_leq(0, pivot - 1) if pivot > 0 else 0
        count2 = count_leq(pivot, n - 1)
        
        return count1 + count2
