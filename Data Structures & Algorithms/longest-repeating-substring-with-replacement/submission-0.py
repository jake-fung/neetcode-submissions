class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        cCount = {}
        for r, c in enumerate(s):
            cCount[c] = cCount.get(c, 0) + 1
            while (r - l - max(cCount.items(), key=lambda i: i[1])[1]) >= k:
                cCount[s[l]] -= 1
                l += 1
            res = max(res, r-l+ 1)
        return res
# X     1   {X: 1}
# XY    2   {X: 1, Y: 1}
# XYY   3   {X: 1, Y: 2}
# XYYX  4   {X: 2, Y: 2}

# A         1
# AA        2
# AAA       3
# AAAB      4
# AAABA     5
# AAABAB    not good    
# AABAB     not good
# ABAB      not good
# BAB       3
# BABB      4


