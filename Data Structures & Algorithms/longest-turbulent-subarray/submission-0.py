class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        result = count = 0
        sign = -1

        for i in range(n-1):
            if arr[i] > arr[i + 1]:
                count = count + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i + 1]:
                count = count + 1 if sign == 1 else 1
                sign = 0
            else:
                count = 0
                sign = -1

            result = max(result, count)

        return result + 1
