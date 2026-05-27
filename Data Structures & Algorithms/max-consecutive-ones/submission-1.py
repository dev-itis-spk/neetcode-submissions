class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count_local = max_count_global = 0
        for num in nums:
            if num:
                max_count_local += 1 
            else:
                max_count_local = 0
            max_count_global = max(max_count_local, max_count_global)
        return max_count_global
        