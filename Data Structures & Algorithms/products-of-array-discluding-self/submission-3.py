class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix array
        prefix, suffix = [1], [1]
        multTemp = 1
        for num in nums:
            multTemp *= num
            prefix.append(multTemp)
        multTemp = 1
        # suffix array
        for num in nums[::-1]:
            multTemp *= num
            suffix.append(multTemp)
        res = []
        for index, num in enumerate(nums):
            resNum = prefix[index] * suffix[len(nums)-index-1]
            res.append(resNum)

        return res