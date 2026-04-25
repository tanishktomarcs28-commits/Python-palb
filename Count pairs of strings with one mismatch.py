from collections import defaultdict

class Solution:
    def countPairs(self, arr):
        pattern_map = defaultdict(int)
        count = 0

        for word in arr:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                
                count += pattern_map[pattern]
                pattern_map[pattern] += 1

        return count
