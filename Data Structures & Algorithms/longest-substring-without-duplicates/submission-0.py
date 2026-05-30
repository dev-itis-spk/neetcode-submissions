class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_string = 0
        L = 0
        win_set = set()

        for R in range(len(s)):
            while s[R] in win_set:
                win_set.remove(s[L])
                L += 1

            win_set.add(s[R])
            max_sub_string = max(max_sub_string, R - L + 1)
        
        return max_sub_string
