class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for c in s:
            if c.isalnum():
                newS += c.lower()
        l = 0
        r = len(newS) - 1
        while l < r:
            print(newS[l], newS[r])
            if newS[l] != newS[r]:
                return False
            l += 1
            r -= 1
        return True