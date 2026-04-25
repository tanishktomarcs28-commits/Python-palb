class Solution:
    def minMen(self, arr):
        #code here 
        n = len(arr)
        intervals = []

        # Step 1: build intervals
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))

        # Step 2: sort by start
        intervals.sort()

        count = 0
        i = 0
        curr_end = 0
        farthest = 0

        # Step 3: greedy covering
        while curr_end < n:
            while i < len(intervals) and intervals[i][0] <= curr_end:
                farthest = max(farthest, intervals[i][1])
                i += 1

            if farthest == curr_end:
                return -1  # cannot extend coverage

            count += 1
            curr_end = farthest + 1

        return count
