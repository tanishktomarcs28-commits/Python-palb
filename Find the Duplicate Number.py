class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
