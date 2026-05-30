class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size, total = len(nums), 0
        prefix = [0] * (size + 1)
        
        for i in range(size):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(size):
            left_sum = prefix[i]
            right_sum = prefix[size] - prefix[i + 1]
            if left_sum == right_sum:
                return i
        return -1
