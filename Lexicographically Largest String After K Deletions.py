class Solution:
    def lexicographicallyLargest(self, s, k):
        stack = []

        for ch in s:
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # if still deletions left
        while k > 0:
            stack.pop()
            k -= 1

        return "".join(stack)
