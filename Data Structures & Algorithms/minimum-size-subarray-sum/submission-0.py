class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sub_size = float('inf')
        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                min_sub_size = min(min_sub_size, R - L + 1)
                curr_sum -= nums[L]
                L += 1

        return 0 if min_sub_size == float('inf') else min_sub_size