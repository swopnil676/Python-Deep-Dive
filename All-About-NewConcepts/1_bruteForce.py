from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        for i in range(n):
            cur = 0

            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)

        return res
    
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

sol = Solution()
print(sol.maxSubArray(nums))

# Subarray: [4, -1, 2, 1]