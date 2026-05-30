class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_string = 0
        L = 0
        maps = {}

        for R in range(len(s)):
            if s[R] in maps:
                L = max(maps[s[R]] + 1, L)
            maps[s[R]] = R
            max_sub_string = max(max_sub_string, R - L + 1)
        return max_sub_string
