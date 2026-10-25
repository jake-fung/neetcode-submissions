class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, res = 0, 0
        for r, num in enumerate(s):
            seen[num] = seen.get(num, 0) + 1
            while seen[num] > 1:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res