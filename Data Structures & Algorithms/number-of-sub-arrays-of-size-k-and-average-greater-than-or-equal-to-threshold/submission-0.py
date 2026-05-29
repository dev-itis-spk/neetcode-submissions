class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = curr_sum = 0

        for R in range(len(arr)):
            curr_sum += arr[R]
            if R >= k-1:
                res += curr_sum >= threshold
                curr_sum -= arr[R - k + 1]
        
        return res
        