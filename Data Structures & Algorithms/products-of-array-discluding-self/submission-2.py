class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, prod, zeroCount = 0, 1, 0
        for n in nums:
            if n == 0:
                zeroCount += 1
                continue
            prod *= n
        if zeroCount > 1:
            return [0] * len(nums)
        res = []
        for n in nums:
            if zeroCount == 1:
                if n == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // n)
        return res