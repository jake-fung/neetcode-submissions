class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        s2Count = {}
        l = 0
        for r, c in enumerate(s2):
            s2Count[c] = s2Count.get(c, 0) + 1
            if s1Count.items() == s2Count.items():
                return True
            while (c in s2Count.keys() and c not in s1Count.keys()) or s2Count.get(c,0) > s1Count[c]:
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1
            print(s2Count)

        return False